import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType 
from pyspark.sql.types import ArrayType, DoubleType, BooleanType
from pyspark.sql.functions import col,array_contains

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.read.csv("/home/ubuntu/dados/Data7602DescendingYearOrder.csv")

df.printSchema()
df.show()

df_n =  df.select('*', (df._c4 + 10).alias('ecPlusTen'))
df_n.show()

