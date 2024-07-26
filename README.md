# Avaliação Técnica - Projeto BI MultiStore

## Cenário
A loja fictícia MultiStore contratou você para criar um processo de Business Intelligence (BI) para as vendas de suas lojas. O cliente enviará semanalmente, via FTP, uma base de dados contendo os principais dados de vendas.

## Tecnologias
- **SQL**
- **Power BI**
- *(Opcional)* **C#** ou outra linguagem de sua preferência

## Tarefas

### 1. Criação do Banco de Dados
- Utilize SQL para criar um banco de dados com um nome à sua escolha, que funcionará como nosso Data Warehouse (DW).
- Inicialmente, crie um esquema denominado `stage` e uma tabela denominada `MultiStore`.

### 2. Script de Importação de Dados (Opcional)
- Desenvolva um script em C# (ou outra linguagem de sua preferência) para ler o arquivo no formato XLSX e importar todos os campos para a tabela `[stage].[MultiStore]`.
- Após a leitura, o arquivo deve ser movido para uma pasta denominada "arquivos processados".
- A cada nova leitura, deve-se excluir os dados anteriores na tabela e inserir os novos dados, juntamente com o nome do arquivo.

### 3. Modelo de Dados e Processo ETL
- A partir do conjunto de dados fornecido, crie um modelo de dados utilizável em uma solução de BI.
- Inclua as principais dimensões e fatos que serão utilizados.
- Utilize procedimentos SQL para a criação do processo ETL (Extração, Transformação e Carga).

### 4. Dashboard no Power BI
- Crie um dashboard no Power BI com as principais informações necessárias para um usuário entender o conjunto de dados.
- Inclua gráficos, tabelas e outros elementos visuais que facilitem a compreensão dos dados.

### 5. KPIs e Visualizações
- Defina alguns KPIs relevantes para o conjunto de dados fornecido.
- Crie visualizações no dashboard para acompanhar o desempenho desses KPIs ao longo do tempo.

### 6. (Bônus) Mineração de Dados
- Utilize técnicas de mineração de dados para identificar padrões ou tendências interessantes no conjunto de dados fornecido.
- Crie visualizações que ajudem a destacar esses padrões ou tendências.

## Critérios de Avaliação
- Avaliaremos a lógica e os conhecimentos em banco de dados, BI e na implementação da linguagem de programação escolhida (C# ou outra).

## Retorno Esperado
- Scripts criados (tabelas, visualizações, procedimentos etc.).
- Dashboard com as métricas e dimensões.
