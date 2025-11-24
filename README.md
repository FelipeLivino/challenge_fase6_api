# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Previsão de Falhas em Equipamentos Industriais com Sensores e IA

## Nome do grupo
Rumo ao NEXT

## 👨‍🎓 Integrantes: 

- Felipe Livino dos Santos (RM 563187)
- Daniel Veiga Rodrigues de Faria (RM 561410)
- Tomas Haru Sakugawa Becker (RM 564147)
- Daniel Tavares de Lima Freitas (RM 562625)
- Gabriel Konno Carrozza (RM 564468)

## 👩‍🏫 Professores:

### Tutor(a)

- Leonardo Ruiz Orabona

### Coordenador(a)

- ANDRÉ GODOI CHIOVATO


## 📜 Descrição

O projeto tem como objetivo desenvolver uma solução inteligente para antecipar falhas em equipamentos industriais por meio de sensores conectados e algoritmos de machine learning. A aplicação será responsável por monitorar continuamente os dados gerados por máquinas, processá-los em tempo real e utilizar modelos preditivos para indicar riscos de falha. Além disso, a plataforma contará com um dashboard interativo para visualização dos dados, índices de falha e status dos equipamentos.

A infraestrutura será baseada em serviços de nuvem, utilizando o Heroku para hospedar a aplicação e o banco de dados PostgreSQL para o armazenamento de dados.

O frontend foi construido usando Streamlit. Toda a lógica será implementada em Python, desde os simuladores até os modelos de previsão.

▶️ [Assista ao vídeo no YouTube](https://www.youtube.com/watch?v=AjQiXNsl79o)

## Arquitetura
  
<image src="assets/arquitetura.png" alt="Arquitetura do projeto" width="100%" height="100%">

A arquitetura do projeto foi desenhada para ser modular e escalável, utilizando uma abordagem baseada em microserviços para desacoplar as responsabilidades e facilitar a manutenção. A seguir, detalhamos os principais componentes da arquitetura:

- **API (Interface de Programação de Aplicações):** A API é o ponto central da nossa arquitetura, responsável por gerenciar todas as comunicações entre o cliente, o banco de dados e os modelos de machine learning. Ela foi desenvolvida em Python utilizando o framework FastAPI, que oferece alta performance e facilidade de uso. A API expõe endpoints para CRUD (Create, Read, Update, Delete) de equipamentos, sensores e leituras de sensores, além de um endpoint para realizar predições de falhas.

- **Banco de Dados:** Utilizamos o PostgreSQL como sistema de gerenciamento de banco de dados relacional. Ele é responsável por armazenar todas as informações sobre os equipamentos, sensores e as leituras coletadas. A escolha pelo PostgreSQL se deu por sua robustez, confiabilidade e suporte a tipos de dados avançados.

- **Modelos de Machine Learning:** Os modelos de machine learning são o coração da nossa solução de predição de falhas. Eles foram treinados para identificar padrões nos dados dos sensores que possam indicar uma falha iminente. O `ModelExecutor.py` é responsável por carregar o modelo treinado (`best_model.pkl`) e realizar as predições com base nos dados recebidos pela API.

- **Wokwi (Simulador de Sensor):** Para simular o ambiente de produção e gerar dados para treinamento e teste, utilizamos o Wokwi, um simulador de hardware online. O `ESP32 NTP Example.ino` é um exemplo de como os sensores podem ser programados para enviar dados para a nossa API.

- **Estrutura do Projeto:** O projeto foi organizado em diretórios que separam as responsabilidades, facilitando a navegação e o desenvolvimento. As principais pastas são: `api` para a lógica da API, `banco_dados` para scripts de banco de dados, `core` para configurações centrais, `crud` para as operações de banco de dados, `model` para os modelos de machine learning, `models` para as representações de dados do SQLAlchemy e `schemas` para os esquemas de validação de dados do Pydantic.

<image src="assets/arquitetura_generalista.png" alt="Arquitetura do projeto" width="100%" height="100%">

## 1. Separação de Responsabilidades e Camadas

| Bloco                   | Boa Prática                                                                 | Justificativa de Mercado                                                                                                                                                                                                                                                                                                      |
|--------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wokwi/ESP32 → FastAPI    | **Desacoplamento da Fonte de Dados:** O dispositivo IoT não se conecta diretamente ao banco de dados; ele envia dados para um *endpoint* da API. | Em ambientes de produção, dispositivos IoT raramente interagem diretamente com o banco por questões de segurança (credenciais de banco) e confiabilidade (o dispositivo precisa de resposta rápida). A API pode atuar como uma **porta de entrada segura**, com futura implementação de login e autenticação. |
| FastAPI → Streamlit      | **Separação Backend/Frontend:** A camada de dados e lógica de negócios (API/ML) é separada da camada de apresentação (Dashboard). | Permite que o *dashboard* (frontend) foque em **visualizar**, enquanto o *backend* (API) processa, armazena e serve inferências. Caso o Streamlit seja trocado por React ou mobile, o *backend* permanece inalterado.                                                                                                    |

## 2. Escolha de Tecnologias

| Tecnologia        | Boa Prática                                                                                     | Justificativa de Mercado                                                                                                                                                                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python + FastAPI  | **Serviço de API Moderno e de Alto Desempenho:** *FastAPI* é assíncrono (ASGI), rápido e nativo para Python. | Escolha padrão para criar **APIs microsservice** com alta concorrência e baixa latência. Ideal para ingestão de dados de sensores e *serving* de modelos de ML. Gera documentação de API (OpenAPI/Swagger) automaticamente, o que é essencial para governança. |
| PostgreSQL        | **Banco de Dados Relacional Confiável:** SGBD robusto e amplamente utilizado.                   | Oferece confiabilidade, integridade de dados (chaves primárias, estrangeiras) e excelente para dados estruturados. É base para consultas SQL complexas, cálculo de KPIs e treino/inferência de ML.                                                           |
| Streamlit         | **Dashboard Rápido para MVP/Protótipo:** Permite construir UIs simples rapidamente.              | Agiliza o desenvolvimento e entrega do MVP, focando na lógica de negócio e não nos KPIs. Permite validar resultados de Machine Learning de forma rápida.                                                                                                   |

## 3. Fluxo de Dados e Processamento


| Fluxo                          | Boa Prática                                                                 | Justificativa de Mercado                                                                                                                                                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transporte Web Service HTTPS   | **Comunicação Segura e Ubíqua:** Utiliza protocolo padrão da web e criptografado. | O HTTPS é o padrão para comunicação pela internet. Embora o MQTT seja usado em IoT, o HTTPS é mais simples de implementar em Wokwi/ESP32 e mais fácil de hospedar em ambientes de nuvem/PaaS como o Heroku.                 |
| Inferência do Algoritmo (na API)| **ML as a Service (MLaaS):** O modelo é carregado e executado diretamente na API (*runtime*). | Garante que as previsões (scores) e a lógica de alerta sejam rápidas e acessíveis no *dashboard*. Essa abordagem é mais comum e eficiente para servir modelos de inferência online.                                          |

## 📌 Resumo da Escolha Arquitetural  

A escolha dessa arquitetura reflete uma solução de mercado **balanceada**, que prioriza a **agilidade** no contexto de um **MVP**, sem sacrificar a **escalabilidade a longo prazo**:

- **Agilidade (FastAPI + Streamlit):**  
  Permite a construção de ponta a ponta (**API + Dashboard**) rapidamente, usando a stack popular do **Python**.

- **Robustez (PostgreSQL + Heroku):**  
  Garante a **persistência** e a **integridade dos dados** em uma plataforma confiável (**Heroku**) com um SGBD maduro (**PostgreSQL**).

- **Coerência (MLaaS):**  
  O modelo de **Machine Learning** é integrado à camada de serviço (**FastAPI**) para que o **dashboard** consiga consumir as inferências de forma eficiente, fechando o ciclo de análise e decisão exigido pelo desafio.

## Links de repositórios e servidor 

Link do repositório de API:  https://github.com/FelipeLivino/challenge_fase6_web

Link do repositório web: https://github.com/FelipeLivino/challenge_fase6_api/tree/main

Link servidor web: https://reply-web-5ff86c92bd5e.herokuapp.com/

Link servidor API: https://reply-api-15a7328429e3.herokuapp.com/

Link Wokiwi: https://wokwi.com/projects/431968269578375169

## 📁 Estrutura de pastas

A estrutura de pastas do projeto foi organizada da seguinte forma:

- **api/:** Contém a lógica da API, dividida em `v1` para a versão 1 da API.
  - **endpoints/:** Define os endpoints da API para cada recurso (equipamento, sensor, leitura de sensor).
- **assets/:** Imagens usadas no readme.
- **banco_dados/:** Armazena scripts SQL para a criação do banco de dados e tabelas.
- **core/:** Contém as configurações centrais do projeto, como a configuração do banco de dados.
- **crud/:** Implementa as operações de CRUD (Create, Read, Update, Delete) para cada entidade do banco de dados.
- **model/:** Contém os modelos de machine learning, incluindo o modelo treinado e o executor do modelo.
- **models/:** Define os modelos de dados do SQLAlchemy, que representam as tabelas do banco de dados.
- **schemas/:** Define os esquemas de validação de dados do Pydantic, utilizados pela API para validar os dados de entrada e saída.
- **wokwi/:** Contém os arquivos do simulador de sensor, incluindo o código do ESP32 e a configuração do projeto.
- **main.py:** Arquivo principal para execução da API.
- **requirements.txt:** Lista as dependências do projeto.
- **Procfile**: arquivo de implantação do Heroku.
- **.envEXAMPLE**: Arquivo para configuração das variaveis de ambiente (remover o EXAMPLE) 
- **postman_collection.json:** Arquivo de configuração do Postman para exibição da API.
- **README.md:** Arquivo de documentação do projeto.

## 🛠️ Tecnologias Utilizadas

🔧 Linguagem de Programação:
-	Python: Backend, FrontEnd, APIs e machine learning.
🌐 Frontend:
-	Streamlit: Framework para construção da interface do usuário.
🧠 Inteligência Artificial:
-	pandas / numpy / scikit-learn: Manipulação e tratamento de dados e treinamento do algoritmo de predição.
☁️ Serviços de Nuvem:
-	Heroku: Plataforma de nuvem como serviço (PaaS) para hospedagem da aplicação.
-	PostgreSQL: Banco de dados relacional.

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

Pré-requisitos:
- DBeaver
- Heroki cli
- Python 3.8+ instalado
- Virtualenv
- fastapi
- uvicorn[standard]
- sqlalchemy
- psycopg2-binary
- python-dotenv
- gunicorn
- pydantic-settings
- joblib
- pandas
- numpy
- scikit-learn

**Ambiente Local** 
1. Crie um ambiente virtual Python: python3 -m venv venv
2. Ative o ambiente virtual: 

  MAC OS / Linux: source venv/bin/activate

  Windows: venv\Scripts\activate
  
3. Instale as dependências: pip install -r requirements.txt
4. Execute o comando para iniciar o servidor: gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app

**HEROKU**
1. Crie um servidor
2. Adicione o add-on PostgreSQL
3. Abra o DBeaver
4. Execute o código de banco de dados banco_dados/arquivo_banco.sql
5. Suba o projeto no Heroku atraves dos comando abaixo **Adapte o link e o nome das pastas**

  heroku login
  git init
  heroku git:remote -a NOME_APLICACAO
  git add .
  git commit -am "first commit"
  git push heroku main

## Decisão de escolha do algoritmo de banco de dados

**Decisão**: Escolhemos o modelo "DecisionTreeClassifier" devido ao excelente desempenho e consumir pouco recurso quanto a utilização de memória.

Model: DecisionTreeClassifier
Accuracy: 1.0
              precision    recall  f1-score   support

      ALERTA       1.00      1.00      1.00        43
      NORMAL       1.00      1.00      1.00        40
      PERIGO       1.00      1.00      1.00        56

    accuracy                           1.00       139
   macro avg       1.00      1.00      1.00       139
weighted avg       1.00      1.00      1.00       139



Model: SVC
Accuracy: 0.5035971223021583
              precision    recall  f1-score   support

      ALERTA       0.53      0.40      0.45        43
      NORMAL       0.40      0.35      0.37        40
      PERIGO       0.54      0.70      0.61        56

    accuracy                           0.50       139
   macro avg       0.49      0.48      0.48       139
weighted avg       0.50      0.50      0.49       139



Model: AdaBoostClassifier
Accuracy: 0.4028776978417266
              precision    recall  f1-score   support

      ALERTA       0.34      1.00      0.51        43
      NORMAL       0.00      0.00      0.00        40
      PERIGO       1.00      0.23      0.38        56

    accuracy                           0.40       139
   macro avg       0.45      0.41      0.30       139
weighted avg       0.51      0.40      0.31       139



Model: LogisticRegression
Accuracy: 0.37410071942446044
              precision    recall  f1-score   support

      ALERTA       0.40      0.19      0.25        43
      NORMAL       0.41      0.30      0.35        40
      PERIGO       0.36      0.57      0.44        56

    accuracy                           0.37       139
   macro avg       0.39      0.35      0.35       139
weighted avg       0.39      0.37      0.36       139



Model: RandomForestClassifier
Accuracy: 1.0
              precision    recall  f1-score   support

      ALERTA       1.00      1.00      1.00        43
      NORMAL       1.00      1.00      1.00        40
      PERIGO       1.00      1.00      1.00        56

    accuracy                           1.00       139
   macro avg       1.00      1.00      1.00       139
weighted avg       1.00      1.00      1.00       139


## Decisão de arquitetura





## 📆 Plano Futuros de Desenvolvimento

Etapas:
1.	API: Implementação de Autenticação
2.	FRONT-END: Implementação de autenticação / Exclusão de dados / melhoria nos alertasa


## 📥 Estratégia de Coleta de Dados

Simulação de Sensores
-	Dados gerados dados no wokwi: temperatura, vibração, umidade.
-	Os dados são enviados para a nossa API.
- Link da aplicação no wokwi: https://wokwi.com/projects/431968269578375169 

## 📊 Justificativa

No setor industrial, falhas inesperadas em equipamentos podem gerar prejuízos significativos devido à paralisação de linhas de produção, manutenção corretiva emergencial e perda de produtividade. Apesar da presença de sensores nos equipamentos, muitas vezes os dados capturados não são utilizados de forma preditiva. Nosso projeto busca transformar esses dados em insights valiosos, utilizando aprendizado de máquina para prever falhas antes que elas ocorram, possibilitando ações preventivas e uma maior eficiência operacional.

O projeto visa entregar uma solução inteligente e escalável para análise preditiva de falhas, aproveitando tecnologias modernas de backend e frontend. A fase inicial foca em levantar a arquitetura, integrar os componentes básicos e montar uma base para aplicação de machine learning.

## Divisão de Responsabilidades (exemplo):

- Membro	Responsabilidade
- Gabriel	Frontend
- Daniel F.	API em Python + Integração com sensores
- Tomas	Simulador de sensores
- Felipe	Configuração do Heroku e PostgreSQL.
- Daniel V.	Modelagem de ML

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
