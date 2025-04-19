# Projeto: Orquestração de Pipeline de Dados na AWS

## 🎯 Objetivo

Desenvolver um pipeline de dados completo na AWS que permita ao administrador do sistema visualizar, consultar, inserir e deletar registros de forma eficiente. Os dados são extraídos de arquivos `.txt` disponibilizados por órgãos governamentais, transformados em formato tabular/JSON e armazenados em uma base estruturada, viabilizando consultas rápidas e modificações dinâmicas através de consultas no banco de dados.

---

## 🛠️ Serviços Utilizados na Solução

### ☁️ Amazon S3
Utilizado como repositório inicial para armazenar os arquivos `.zip` recebidos. Após a descompactação, os arquivos `.txt` são armazenados em buckets organizados para facilitar o processamento posterior.

### 🧑‍💻 AWS Cloud9
Ambiente de desenvolvimento em nuvem usado para testar e validar localmente os scripts e funções antes de colocá-los em produção, garantindo maior confiabilidade e controle no processo de desenvolvimento.

### ⚙️ AWS Lambda
Responsável por executar automaticamente funções escritas em Python, que realizam:

- A descompactação dos arquivos `.zip` armazenados no S3
- O tratamento e envio dos dados extraídos para o banco de dados DynamoDB

### 🧬 AWS Glue Crawler
Ferramenta utilizada para mapear e catalogar os dados provenientes dos arquivos `.txt`, identificando os tipos e estruturas dos dados. Isso permite a criação de tabelas que facilitam a consulta e a transformação dos dados posteriormente.

### 🗃️ Amazon DynamoDB
Banco de dados NoSQL utilizado para armazenar os dados em formato tabular/JSON. Ele permite operações de leitura, inserção, atualização e exclusão (CRUD), além de possibilitar consultas rápidas e escaláveis sobre grandes volumes de dados.

---

## 🧩 Visão Geral da Solução

A arquitetura proposta permite a orquestração completa do fluxo de dados, desde a ingestão dos arquivos brutos até sua disponibilização em um banco estruturado para consultas SQL e manipulação dos registros. Todo o processo é automatizado por funções Lambda, garantindo escalabilidade, economia e baixa necessidade de intervenção manual.

---

## 🗺️ Diagrama da Solução

```mermaid
graph TD
    A[Arquivos .zip do Governo] --> B[S3 - Bucket de Entrada]
    B --> C[Lambda - Descompactação]
    C --> D[S3 - Arquivos .txt]
    D --> E[Glue Crawler - Mapeamento dos Dados]
    E --> F[DynamoDB - Base Tabular/JSON]
    F --> G[Consultas SQL / CRUD via Aplicação]
