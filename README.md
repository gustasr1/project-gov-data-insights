# 📊 Análise de Gastos: Cartões Corporativos do Governo Federal (CPGF)

## 🎯 Objetivo do Projeto
Este projeto tem como objetivo realizar a extração, limpeza, transformação e análise exploratória dos dados abertos referentes aos gastos com Cartões de Pagamento do Governo Federal (CPGF). O foco é gerar *insights* sobre a distribuição do orçamento, identificar os maiores gastadores da máquina pública e calcular os índices de transparência (gastos identificados vs. gastos sigilosos/saques em espécie).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** Pandas (Manipulação e Limpeza de Dados)
* **Ambiente:** VS Code / Jupyter Notebook

## 🗂️ Estrutura do Repositório
Para manter a organização e as boas práticas, os arquivos estão divididos da seguinte forma:

* `data/raw/`: Arquivos CSV originais brutos, sem tratamento.
* `data/processed/`: Arquivos CSV limpos, tipados e prontos para o BI (`cpgf_limpo.csv`).
* `notebooks/`: Notebooks contendo o passo a passo da exploração e limpeza.
* `README.md`: Documentação do projeto.

## 🧹 Etapas de Processamento (Data Cleaning)
A base de dados passou por um rigoroso processo de tratamento para garantir a qualidade da análise, incluindo:
* **Tratamento de Nulos e Sigilo:** Identificação e preenchimento adequado de CPFs vazios referentes a saques e despesas sigilosas.
* **Conversão de Tipos:** Transformação de textos financeiros em decimais (`float64`), padronização de calendários (`datetime`) e proteção de códigos identificadores (CPFs/CNPJs) como texto.
* **Otimização de Memória:** Conversão de colunas repetitivas para o tipo `category`, reduzindo o peso do *dataframe*.
* **Padronização de Strings:** Remoção de espaços invisíveis (`.strip()`) e padronização para letras maiúsculas/minúsculas.

## 📈 Análise Exploratória (Perguntas de Negócio Respondidas)
Durante a fase de EDA (Exploratory Data Analysis), os dados responderam às seguintes perguntas:
1. Qual o volume financeiro e o percentual de transparência dos gastos (Identificados vs. Sigilosos)?
2. Quais são os Ministérios (Órgãos Superiores) com o maior volume de gastos totais e sigilosos?
3. Quais são os Órgãos Subordinados campeões de uso do cartão corporativo?
4. Quais empresas e pessoas físicas mais faturaram recebendo dinheiro dos cartões?

## 🚀 Como Executar o Projeto
1. Clone este repositório: `git clone https://github.com/gustasr1/project-gov-data-insights.git`
2. Instale as dependências: `pip install pandas`
3. Execute o notebook principal localizado na pasta `notebooks/` para visualizar o passo a passo.
