from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession


myconf = SparkConf()

myconf.set("spark.master","local[2]")
myconf.set("spark.app.name","joins")

"""
###myconf = SparkConf()

myconf.set("spark.app.name","session_18_windowaggregations")
myconf.set("spark.master","local[2]")

"""
spark = SparkSession.builder.config(conf=myconf).getOrCreate()

ordersDf = (spark.read.format("csv").option("header",True).option("path","D://<>//datasets_for_practice//orders.csv")).load()

customersDf = (spark.read.format("csv").option("header",True).option("path","D://<>//customers.csv")).load()

#customersDf.show()
joinCondition = ordersDf.order_customer_id == customersDf.customer_id
joinDf = ordersDf.join(customersDf,joinCondition,"inner")
joinDf.show()


"""
+--------+--------------------+-----------------+---------------+-----------+--------------+--------------+--------------+-----------------+--------------------+-------------+--------------+----------------+
|order_id|          order_date|order_customer_id|   order_status|customer_id|customer_fname|customer_lname|customer_email|customer_password|     customer_street|customer_city|customer_state|customer_zipcode|
+--------+--------------------+-----------------+---------------+-----------+--------------+--------------+--------------+-----------------+--------------------+-------------+--------------+----------------+
|       1|2013-07-25 00:00:...|            11599|         CLOSED|      11599|          Mary|        Malone|     XXXXXXXXX|        XXXXXXXXX|8708 Indian Horse...|      Hickory|            NC|           28601|
|       2|2013-07-25 00:00:...|              256|PENDING_PAYMENT|        256|         David|     Rodriguez|     XXXXXXXXX|        XXXXXXXXX|7605 Tawny Horse ...|      Chicago|            IL|           60625|
|       3|2013-07-25 00:00:...|            12111|       COMPLETE|      12111|         Amber|        Franco|     XXXXXXXXX|        XXXXXXXXX|8766 Clear Prairi...|   Santa Cruz|            CA|           95060|
|       4|2013-07-25 00:00:...|             8827|         CLOSED|       8827|         Brian|        Wilson|     XXXXXXXXX|        XXXXXXXXX|   8396 High Corners|  San Antonio|            TX|           78240|
|       5|2013-07-25 00:00:...|            11318|       COMPLETE|      11318|          Mary|         Henry|     XXXXXXXXX|        XXXXXXXXX|3047 Silent Ember...|       Caguas|            PR|           00725|
|       6|2013-07-25 00:00:...|             7130|       COMPLETE|       7130|         Alice|         Smith|     XXXXXXXXX|        XXXXXXXXX|      8852 Iron Port|     Brooklyn|            NY|           11237|
|       7|2013-07-25 00:00:...|             4530|       COMPLETE|       4530|          Mary|         Smith|     XXXXXXXXX|        XXXXXXXXX|1073 Green Leaf G...|        Miami|            FL|           33161|
|       8|2013-07-25 00:00:...|             2911|     PROCESSING|       2911|          Mary|         Smith|     XXXXXXXXX|        XXXXXXXXX|9166 Golden Necta...|       Caguas|            PR|           00725|
|       9|2013-07-25 00:00:...|             5657|PENDING_PAYMENT|       5657|          Mary|         James|     XXXXXXXXX|        XXXXXXXXX|  1389 Dusty Circuit|     Lakewood|            OH|           44107|
|      10|2013-07-25 00:00:...|             5648|PENDING_PAYMENT|       5648|        Joshua|         Smith|     XXXXXXXXX|        XXXXXXXXX|864 Iron Spring S...|      Memphis|            TN|           38111|
|      11|2013-07-25 00:00:...|              918| PAYMENT_REVIEW|        918|        Nathan|         Smith|     XXXXXXXXX|        XXXXXXXXX|    9627 Honey Trail|       Caguas|            PR|           00725|
|      12|2013-07-25 00:00:...|             1837|         CLOSED|       1837|          Mary|          Vega|     XXXXXXXXX|        XXXXXXXXX|  4312 Bright Corner|       Caguas|            PR|           00725|
|      13|2013-07-25 00:00:...|             9149|PENDING_PAYMENT|       9149|        Ronald|     Whitehead|     XXXXXXXXX|        XXXXXXXXX|6789 Round Robin ...|    Santa Ana|            CA|           92705|
|      14|2013-07-25 00:00:...|             9842|     PROCESSING|       9842|          Mary|         Smith|     XXXXXXXXX|        XXXXXXXXX|454 Lazy Branch F...|       Caguas|            PR|           00725|
|      15|2013-07-25 00:00:...|             2568|       COMPLETE|       2568|         Maria|         Smith|     XXXXXXXXX|        XXXXXXXXX|   3544 Fallen Mount|      Memphis|            TN|           38127|
|      16|2013-07-25 00:00:...|             7276|PENDING_PAYMENT|       7276|        Pamela|         Smith|     XXXXXXXXX|        XXXXXXXXX|    9243 Old Gardens|       Caguas|            PR|           00725|
|      17|2013-07-25 00:00:...|             2667|       COMPLETE|       2667|         Tammy|         Smith|     XXXXXXXXX|        XXXXXXXXX|   8906 Rustic Mall |   Sun Valley|            CA|           91352|
|      18|2013-07-25 00:00:...|             1205|         CLOSED|       1205|          Mary|        Powell|     XXXXXXXXX|        XXXXXXXXX|9299 Quiet Pionee...|        Miami|            FL|           33126|
|      19|2013-07-25 00:00:...|             9488|PENDING_PAYMENT|       9488|          Mary|         Smith|     XXXXXXXXX|        XXXXXXXXX|    9758 Foggy Range|      Hialeah|            FL|           33012|
|      20|2013-07-25 00:00:...|             9198|     PROCESSING|       9198|         David|          Kerr|     XXXXXXXXX|        XXXXXXXXX|7312 Crystal Will...|Bowling Green|            KY|           42101|
+--------+--------------------+-----------------+---------------+-----------+--------------+--------------+--------------+-----------------+--------------------+-------------+--------------+----------------+
only showing top 20 rows
"""


