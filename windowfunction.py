from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import sum

myconf = SparkConf()

myconf.set("spark.app.name","session_18_windowaggregations")
myconf.set("spark.master","local[2]")

spark = SparkSession.builder.config(conf=myconf).getOrCreate()

invoiceDF = (spark.read.format("csv").\
    option("inferSchema",True).\
    option("path","D://<>//datasets_for_practice//windowdata.csv")\
    .load())

invoiceHeaderDF = invoiceDF.toDF("country","weeknum","numofinvoices","totalquantity","invoicevalue")

# Problem Statement is to calculate the running total of invoice value for each country

myWindowDF = Window.partitionBy("country").orderBy("weeknum").rowsBetween(Window.unboundedPreceding,Window.currentRow)
#unboundedPreceding - would be from the start of the window.. so here for germany it would be 3309.75 for calculating weeknum 51 row
myDF = invoiceHeaderDF.withColumn("RunningTotal",sum("invoicevalue").over(myWindowDF))

myDF.show()

"""
+-------+-------+-------------+-------------+------------+------------------+
|country|weeknum|numofinvoices|totalquantity|invoicevalue|      RunningTotal|
+-------+-------+-------------+-------------+------------+------------------+
| Sweden|     50|            3|         3714|      2646.3|            2646.3|
|Germany|     48|           11|         1795|     3309.75|           3309.75|
|Germany|     49|           12|         1852|     4521.39|           7831.14|
|Germany|     50|           15|         1973|     5065.79|          12896.93|
|Germany|     51|            5|         1103|     1665.91|          14562.84|
| France|     48|            4|         1299|     2808.16|           2808.16|
| France|     49|            9|         2303|     4527.01|           7335.17|
| France|     50|            6|          529|      537.32|           7872.49|
| France|     51|            5|          847|     1702.87|           9575.36|

"""
