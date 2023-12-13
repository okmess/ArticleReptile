from pyspark.sql import SparkSession
import json
import pandas as pd

sparkSession=SparkSession.builder\
                         .appName("local[*]")\
                         .config("spark.sql.shuffle.partitions",4)\
                         .getOrCreate()
sparkSession.conf.set("spark.sql.repl.eagerEval.enabled", "true")
sc=sparkSession.sparkContext

# with open("ACM_journal_final_data.json", "r") as file:
#     data = json.load(file)

with open("IEEE_journal1.json", "r") as file:
    data = json.load(file)
rdd=sc.parallelize(data)

rdd1=rdd.map(lambda data: (data['journal_name'],data['keywords']))
rdd2=rdd1.reduceByKey(lambda a,b: a+'[]'+b)
for key,value_list in rdd2.collect():
    rdd3=sc.parallelize(value_list.split('[]'))
    rdd4=rdd3.groupBy(lambda data: data).map(lambda data:(data[0],list(data[1])))
    rdd5=rdd4.map(lambda data:(data[0],len(data[1])))
    rdd5=rdd5.sortBy(lambda data: data[1],ascending=False)
    df=sparkSession.createDataFrame(rdd5,schema=['keywords','counts'])
    print(key+"期刊中论文提及关键字频次:")
    pdf=df.toPandas()
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(pdf)
        print()