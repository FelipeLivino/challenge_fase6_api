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

A infraestrutura será baseada em serviços da AWS, com uso de EC2 em auto scaling para suportar APIs e simuladores de sensores, SQS para fila de mensagens e tarefas, RDS com PostgreSQL ou MySQL para o banco de dados, ElastiCache para armazenar o estado atual dos equipamentos.

O frontend será construído com React e Next.js, utilizando Chart.js para a exibição dos dashboards e indicadores. Toda a lógica será implementada em Python, desde os simuladores até os modelos de previsão.

## Arquitetura

<image src="assets/arquitetura.png" alt="Arquitetura do projeto" width="100%" height="100%">

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

assets: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

document: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

src: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

main.py: Arquivo principal para execução do sistema.

README.md: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🛠️ Tecnologias Utilizadas

🔧 Linguagem de Programação:
-	Python: Backend, simulação de sensores, APIs e machine learning.
-	JavaScript (TypeScript): Frontend com Next.js + React.
🌐 Frontend:
-	Next.js + React: Framework para construção do frontend.
-	Chart.js: Exibição de dashboards com gráficos dinâmicos.
🧠 Inteligência Artificial:
-	pandas / numpy: Manipulação e tratamento de dados.
☁️ Serviços de Nuvem (AWS):
-	EC2 + Auto Scaling Group: Hospedagem de APIs e simulações.
-	Amazon RDS: Banco de dados relacional (PostgreSQL ou MySQL).
-	Amazon SQS: Fila para comunicação assíncrona entre sensores e APIs.
-	Amazon ElastiCache (Redis): Armazenar cache com o estado atual dos equipamentos.

## 📆 Plano Inicial de Desenvolvimento

Etapas:
1.	Frontend – Setup do Next.js + Chart.js.
2.	Sensores – Criação dos scripts simuladores em Python.
3.	API – Desenvolvimento da API que recebe e processa dados dos sensores.
4.	Banco de Dados – Estruturação do RDS (PostgreSQL ou MySQL).
5.	Cache – Integração com ElastiCache (Redis).
6.	Modelagem de ML – Modelos de previsão de falha.
7.	Dashboard – Exibição dos dados e previsões no frontend.


## 📥 Estratégia de Coleta de Dados

Simulação de Sensores
-	Utilizaremos scripts Python que simulam sensores industriais.
-	Serão gerados dados como: temperatura, vibração, tempo de uso, ciclos de operação, etc.
-	Os dados serão enviados periodicamente para uma fila no Amazon SQS, que será processada pela API.

## 📊 Justificativa

No setor industrial, falhas inesperadas em equipamentos podem gerar prejuízos significativos devido à paralisação de linhas de produção, manutenção corretiva emergencial e perda de produtividade. Apesar da presença de sensores nos equipamentos, muitas vezes os dados capturados não são utilizados de forma preditiva. Nosso projeto busca transformar esses dados em insights valiosos, utilizando aprendizado de máquina para prever falhas antes que elas ocorram, possibilitando ações preventivas e uma maior eficiência operacional.

O projeto visa entregar uma solução inteligente e escalável para análise preditiva de falhas, aproveitando o ecossistema da AWS e tecnologias modernas de backend e frontend. A fase inicial foca em levantar a arquitetura, integrar os componentes básicos e montar uma base para aplicação de machine learning.

## ✅ Funcionalidades previstas

- Dashboard com índices de falha
- Previsão de risco com base em sensores (ML)
- APIs para ingestão de dados
- Simuladores de sensores
- Cache do estado atual dos equipamentos

## Divisão de Responsabilidades (exemplo):

- Membro	Responsabilidade
- Gabriel	Frontend + Charts
- Daniel F.	API em Python + Integração com sensores
- Tomas	Simulador de sensores + Envio para SQS
- Felipe	Configuração da AWS (EC2, SQS, RDS)
- Daniel V.	Modelagem de ML + Redis

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

_Pré-requisitos:_

- Python 3.8+ instalado
- PostgreSQL ou MySQL instalado, ou uma instância RDS configurada
- Node.js e npm/yarn para o frontend
- AWS CLI configurada (opcional para testes em nuvem)

## 🗃 Histórico de lançamentos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
