from pyspark.sql import SparkSession
import json
from datetime import datetime
# .appName("local[*]")\
time1 = datetime.now()
sparkSession=SparkSession.builder\
                         .appName("local[*]")\
                         .config("spark.sql.shuffle.partitions",4)\
                         .getOrCreate()
sparkSession.conf.set("spark.sql.repl.eagerEval.enabled", "true")
sc=sparkSession.sparkContext

with open("/spark-data/journal_final_data_copy_10.json", "r") as file:
    data = json.load(file)
rdd=sc.parallelize(data)

rdd1=rdd.map(lambda data: (data['journal_name'],data['keywords'].split('[]')))

def func1(data):
    result=[]
    for i in range(len(data[1])):
        temp=(data[0],data[1][i])
        result.append(temp)
    return result
rdd2=rdd1.flatMap(func1)
df=sparkSession.createDataFrame(rdd2,schema=['journal_name','keywords'])
df.createTempView("journal")
df1=sparkSession.sql("""select journal_name,keywords,count(*) as count 
                    from journal
                    group by journal_name,keywords
                    order by journal_name,count(*) desc""")
df1.show()
time2 = datetime.now()
print("总耗时" + str(time2 - time1))