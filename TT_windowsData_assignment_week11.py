""" Question 
Problem 1: We have a file windowdata.csv and the field names are country, weeknum, numinvoices, totalquantity, invoicevalue
Step 1: create spark session
Step 2: set the logging level to error
Step 3:   Using the standard dataframe reader API load the file and create a dataframe.Note: The schema should be provided using StructType (do not use infer schema)
Step 4:   Use the standard dataframe writer api to save it in parquet format. While saving make sure data is stored where we should have a folder for each country, weeknum (combination)
Step 5:  Also use the dataframe write api to save the data in Avro format. While saving make sure data is stored where we should have a folder for each country.
"""


from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql.types import StructField, StringType, IntegerType, StructType, FloatType

my_conf = SparkConf()

my_conf.set("spark.app.name","week11_assignment")
my_conf.set("spark.master","local[*]")

spark = SparkSession.builder.config(conf=my_conf).getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

window_data_schema = StructType([
    StructField("country",StringType()),
    StructField("weeknum",IntegerType()),
    StructField("numinvoices",IntegerType()),
    StructField("totalquantity",IntegerType()),
    StructField("invoicevalue",FloatType())

])
window_datadf = (spark.read
                 .format("csv")
                 .schema(window_data_schema)
                 .option("path","D:/trendytech/Week 11/Assignments and DataSets/windowdata.csv")
                 .load())

(window_datadf.write.mode("overwrite").format("parquet")
 .partitionBy("weeknum","country").save("D:/trendytech/Week 11/Assignments and DataSets/windowData/"))
 
 
