// Learn about the ESP32 WiFi simulation in
// https://docs.wokwi.com/guides/esp32-wifi
#include <DHT.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <uri/UriBraces.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

//módulos para webservice
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <string>


class TimeUtil {
public:

  String getISO8601Time() {
    struct tm timeinfo;
    
    if(!getLocalTime(&timeinfo)){
      return ""; 
    }

    char timeBuffer[24]; 
    strftime(timeBuffer, sizeof(timeBuffer), "%Y-%m-%dT%H:%M:%S", &timeinfo);

    // Adiciona o ".000Z" (Milissegundos e fuso horário Z para UTC ou o fuso configurado)
    String isoTime = String(timeBuffer) + ".000Z";
    
    return isoTime;
  }
};

// Instância global renomeada para evitar conflito com a função time() nativa do ESP32
TimeUtil timeManager; 
LiquidCrystal_I2C LCD = LiquidCrystal_I2C(0x27, 16, 2);

const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = -3 * 3600; // Fuso Horário GMT-3 (Brasília)
const int daylightOffset_sec = 0; // Sem horário de verão

//Tempo para coleta das informações
#define INTERVALO_WEBSERVICE 10000
#define INTERVALO_COLETA_MS 5000
unsigned long ultimoTempoColeta = 0;
unsigned long ultimoTempoEnvioWebservice = 0;


#define dhtPino 14 // Pino do sensor DHT22
#define DHT_TIPO DHT22

DHT dht(dhtPino, DHT22); 
Adafruit_MPU6050 mpu;


// --- CONFIGURAÇÕES DE CALIBRAÇÃO E MONITORAMENTO ---
const int AMOSTRAS_CALIBRACAO = 2; // Número de leituras para estabelecer a baseline
float baselineVibracaoMedia = 0.0;  // Armazena a vibração média normal
float limiteAlerta = 0.0;      // Limite para um alerta de vibração (ex: 1.5x a baseline)
float limitePerigo = 0.0;      // Limite para um alerta de perigo (ex: 2.5x a baseline)

// Variáveis de controle de estado
int contadorAmostras = 0;
bool calibrando = true; 

//Variaveis com informacoes da maquina e do sensor
const int equipamentoId = 2;
const int sensorId = 1;

//método http para passar dados dos sensores no web-service
HTTPClient http; 

// ----------------------------------------------------
// FUNÇÃO SPINNER
// ----------------------------------------------------
void spinner() {
 static int8_t counter = 0;
 const char* glyphs = "\xa1\xa5\xdb";
 LCD.setCursor(15, 1);
 LCD.print(glyphs[counter++]);
 if (counter == strlen(glyphs)) {
  counter = 0;
 }
}

// ----------------------------------------------------
// SETUP
// ----------------------------------------------------
void setup() {
 Serial.begin(115200);
 while (!Serial) delay(10);

 LCD.init();
 LCD.backlight();
 LCD.setCursor(0, 0);
 LCD.print("Conectando ao ");
 LCD.setCursor(0, 1);
 LCD.print("WiFi ");

 WiFi.begin("Wokwi-GUEST", "", 6);
 while (WiFi.status() != WL_CONNECTED) {
  delay(250);
  spinner();
 }

 dht.begin();

 LCD.clear();
 LCD.setCursor(0, 0);
 LCD.println("Online");
 LCD.setCursor(0, 1);
 LCD.println("Atualizar Hora");

 // Configura o fuso horário para a sincronização NTP
 configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
 
 Wire.begin(21, 22);
 

 while (!mpu.begin()) {
  LCD.clear();
  LCD.setCursor(0, 0);
  LCD.println("Falha MPU6050");
  delay(1000); // Aguarda 1 segundo antes de tentar novamente
 }

 mpu.setAccelerometerRange(MPU6050_RANGE_2_G);

 LCD.clear();
 LCD.setCursor(0, 0);
 LCD.println("Iniciando");
 LCD.setCursor(0, 1);
 LCD.print("Calibracao");
}

// ----------------------------------------------------
// LOOP
// ----------------------------------------------------
void loop() {
 if (millis() - ultimoTempoColeta >= INTERVALO_COLETA_MS) {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  // Verifica se houve erro na leitura do DHT22
  if (isnan(temperatura) || isnan(umidade)) {
   LCD.clear();
   LCD.setCursor(0, 0);
   LCD.println("Falha DHT22");
   return;
  }
  acelerometroFuncionamento(temperatura, umidade);
  ultimoTempoColeta = millis();
 }
}

// ----------------------------------------------------
// FUNÇÃO ACELEROMETRO
// ----------------------------------------------------
void acelerometroFuncionamento(float temperatura, float umidade){
 sensors_event_t a, g, temp;
 mpu.getEvent(&a, &g, &temp);

 if(temperatura > 40 || temperatura < -20){
  LCD.clear();
  LCD.setCursor(0, 0);
  if(temperatura > 40)
   LCD.println("Temperatura Alta");
  else
   LCD.println("Temperatura Baixa");
  LCD.setCursor(0,1);
  LCD.println("Desligue equipamento");
  callWs("PERIGO", temperatura, umidade, 0.0);
  return;
 }

 if(umidade > 95 || umidade < 15){
  LCD.clear();
  LCD.setCursor(0, 0);
  if(umidade > 95)
   LCD.println("Umidade Alta");
  else
   LCD.println("Umidade Baixa");
  LCD.setCursor(0,1);
  LCD.println("Desligue equipamento");
  callWs("PERIGO", temperatura, umidade, 0.0);
  return;
 }

 char* status = "";
 float x = a.acceleration.x;
 float y = a.acceleration.y;
 float z = a.acceleration.z;
 float vibracaoAtual = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));

 if (calibrando) {
  LCD.clear();
  LCD.setCursor(0, 0);
  LCD.println("Calibrando... ");
  LCD.setCursor(0, 1);
  LCD.print("[Amostra ");
  LCD.print(contadorAmostras + 1);
  LCD.print("/");
  LCD.print(AMOSTRAS_CALIBRACAO);
  LCD.print("] -");
  LCD.print(vibracaoAtual);

  baselineVibracaoMedia += vibracaoAtual;
  contadorAmostras++;

  if (contadorAmostras >= AMOSTRAS_CALIBRACAO) {
   baselineVibracaoMedia = baselineVibracaoMedia / AMOSTRAS_CALIBRACAO;
   
   limiteAlerta = baselineVibracaoMedia * 1.5; 
   limitePerigo = baselineVibracaoMedia * 2.5;

   calibrando = false;
   LCD.clear();
   LCD.setCursor(0, 0);
   LCD.println("Calibracao");
   LCD.setCursor(0, 1);
   LCD.println("concluida");
  }
  Serial.println("## 1 ");
 } else {
  LCD.clear();
  LCD.setCursor(0, 0);
  LCD.print("Vibracao: ");
  LCD.print(vibracaoAtual);
  LCD.setCursor(0, 1);

  Serial.println("## 2 ");
  if (vibracaoAtual > limitePerigo) {
   status = "PERIGO";
   LCD.print("PERIGO! DESLIGAR");
  } else if (vibracaoAtual > limiteAlerta) {
   status = "ALERTA";
   LCD.print("Status: Alerta!");
  } else {
   status = "NORMAL";
   LCD.print("Status: Normal");
  }
 }

 if (!calibrando && millis() - ultimoTempoEnvioWebservice >= INTERVALO_WEBSERVICE) {
  callWs(status, temperatura, umidade, vibracaoAtual);
  ultimoTempoEnvioWebservice = millis();
 }
}


// ----------------------------------------------------
// FUNÇÃO CALLWS (Web Service)
// ----------------------------------------------------
void callWs(char* status, float temperatura, float umidade, float vibracaoAtual ){
 //link do webservice
 http.begin("https://reply-api-15a7328429e3.herokuapp.com/api/v1/leituras_sensores/"); 
 http.addHeader("Content-Type", "application/json");
 
 // LINHA CORRIGIDA: Usando a instância "timeManager"
 String timestamp = timeManager.getISO8601Time(); 
 
 //formar arquivo json
 StaticJsonDocument<1024> doc;
 doc["temperatura"] = temperatura;
 doc["umidade"] = umidade;
 doc["vibracao"] = vibracaoAtual;
 doc["t_equipamento_id"] = equipamentoId;
 doc["t_sensor_id"] = sensorId;
 doc["data_coleta"] = timestamp;

 String httpRequestData;
 serializeJson(doc, httpRequestData);

 int httpResponseCode = http.POST(httpRequestData);
 if (httpResponseCode > 0) {
  Serial.printf("Código de Resposta HTTP: %d\n", httpResponseCode);
  String payload = http.getString();
  Serial.println("Resposta: " + payload);
 } else {
  Serial.printf("Falha na requisição HTTP, erro: %s\n", http.errorToString(httpResponseCode).c_str());
 }
}