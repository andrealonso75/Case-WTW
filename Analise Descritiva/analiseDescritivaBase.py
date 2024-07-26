# Databricks notebook source
# MAGIC %md # Este notebook tem como finalidade fazer uma análise descritiva do dataframe antes de começar o processo de ETL.

# COMMAND ----------

!pip install openpyxl

# COMMAND ----------

# Manipulação de dados

from datetime import datetime

from pyspark.sql.functions import col, date_sub, to_date, round, lit, year, when, regexp_replace, sum, avg, unix_timestamp, concat, to_timestamp, expr, sha1, count, min, max, row_number, hour, minute, second, date_format, format_string, explode, sequence, month, day, col, countDistinct, current_date, datediff, collect_list
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import pandas as pd
import pyspark.pandas as ps

from openpyxl import Workbook

# Warnings
import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

# MAGIC %md ## Lendo a base de dados

# COMMAND ----------

df = ps.read_excel("/Volumes/silver/sisrem/treino/stage_MultiStore.xlsx")

df = df.to_spark()


# COMMAND ----------

# MAGIC %md # Analise básica das informações

# COMMAND ----------

df.describe().display()

# COMMAND ----------

# MAGIC %md Neste df não temos dados nulos, então podemos seguir com o processo

# COMMAND ----------

# MAGIC %md # Entendendo os dados

# COMMAND ----------

# MAGIC %md ## Há mais de um gerente por loja?

# COMMAND ----------

df.groupBy("Regional Manager ID","City").agg(countDistinct("City")).display()

# COMMAND ----------

# MAGIC %md Temos apenas um gerente por loja. Então daqui irão sair duas tabelas:
# MAGIC
# MAGIC 1. dimStore
# MAGIC 2. dimManager

# COMMAND ----------

# MAGIC %md ## As colunas de idade e data de aniversário fazem sentido?

# COMMAND ----------

df.groupBy("Customer Name", "Customer ID", "Customer State").agg(count("Customer Birthday"),count("Customer Age")).display()

# COMMAND ----------

# MAGIC %md Há 793 clientes diferentes na base, porém apenas 5 contém um único registro de idade. Está coluna está descartada assim como a coluna de idade. \
# MAGIC Além disso, todos os clientes dessa base estão ativos. \
# MAGIC Com isso já podemos ter uma ideia que a base de clientes contará com: 
# MAGIC 1. Customer ID -> customerId
# MAGIC 2. Customer Name -> customerName
# MAGIC 3. Customer State -> IsActive
# MAGIC     1. Aqui, vai ser transformada em coluna booleana.

# COMMAND ----------

# MAGIC %md # Concluindo:
# MAGIC
# MAGIC O modelo de dados irá contar com 4 bases de dimensão e uma de fato. As bases de dimensão são bases de dados que contam com características de alguma coisa. Aqui são características de vendas em lojas ao redor dos Estados Unidos.
# MAGIC
# MAGIC Logo as tabelas já definidas serão essas:
# MAGIC
# MAGIC 1. DimCustomer
# MAGIC     1. Customer Id > customerId
# MAGIC     2. Custumer Name > custumerName
# MAGIC     3. Custumer State > isCustumerActive
# MAGIC
# MAGIC 2. DimManager
# MAGIC     1. Regional Manager ID > managerId
# MAGIC     2. Regional Manager > managerName
# MAGIC
# MAGIC 3. DimProduct
# MAGIC     1. Product Id > productId
# MAGIC     2. Category > category
# MAGIC     3. Sub-Category > subCategory
# MAGIC     4. Product Name > productName
# MAGIC
# MAGIC 4. DimStore
# MAGIC     1. Regional Manager ID > ManagerID
# MAGIC     2. Country > country
# MAGIC     3. State > state
# MAGIC     4. City > city
# MAGIC     5. Region > region
# MAGIC     6. Postal Code > postalCode
# MAGIC
# MAGIC 5. FactOrders
# MAGIC     1. Order Id > orderId
# MAGIC     2. Order Date > orderDate
# MAGIC     3. Ship date > shipDate
# MAGIC     4. Ship Mode > shipMode
# MAGIC     5. Customer Id > customerId
# MAGIC     6. Segment > segment
# MAGIC     7. Regional Manager ID > managerId
# MAGIC     8. Product ID > productId
# MAGIC     9. Sales > orderPrice
# MAGIC     10. Quantity > Quantity
# MAGIC     11. Discount > discount
# MAGIC     12. Profit > profit

# COMMAND ----------

df.groupBy("Country", "State","City", "Region","Postal Code").agg(countDistinct("City")).display()
