import pyspark,time,platform,sys,os
from datetime import datetime
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col,lit,current_timestamp
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import inspect,create_engine
from pandas.io import sql
import warnings,matplotlib
from pyspark.sql.window import Window
from pyspark.sql.functions import sum as sum1

warnings.filterwarnings("ignore")
t0 = time.time()
con = create_engine("mysql://root:1q2w3e@localhost/spark")
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName("Hi").getOrCreate()
if 1 == 1:
    w = Window.partitionBy(lit(1)).orderBy("№").rowsBetween(Window.unboundedPreceding, Window.currentRow)
    index = 1
    sql.execute("""drop table if exists `hw_4_1`""", con)
    sql.execute("""drop table if exists `hw_4_2`""", con)
    sql.execute("""drop table if exists `hw_4_3`""", con)
    sql.execute("""CREATE TABLE `hw_4_1` (
                     `№` INT(10) NULL DEFAULT NULL,
                     `Месяц` DATE NULL DEFAULT NULL,
                     `Сумма платежа` FLOAT NULL DEFAULT NULL,
                     `Платеж по основному долгу` FLOAT NULL DEFAULT NULL,
                     `Платеж по процентам` FLOAT NULL DEFAULT NULL,
                     `Остаток долга` FLOAT NULL DEFAULT NULL,
                     `Проценты` FLOAT NULL DEFAULT NULL,
                     `Долг` FLOAT NULL DEFAULT NULL
                  )
                  COLLATE='utf8mb4_0900_ai_ci'
                  ENGINE=InnoDB""", con)
    sql.execute("""CREATE TABLE `hw_4_2` (
                     `№` INT(10) NULL DEFAULT NULL,
                     `Месяц` DATE NULL DEFAULT NULL,
                     `Сумма платежа` FLOAT NULL DEFAULT NULL,
                     `Платеж по основному долгу` FLOAT NULL DEFAULT NULL,
                     `Платеж по процентам` FLOAT NULL DEFAULT NULL,
                     `Остаток долга` FLOAT NULL DEFAULT NULL,
                     `Проценты` FLOAT NULL DEFAULT NULL,
                     `Долг` FLOAT NULL DEFAULT NULL
                  )
                  COLLATE='utf8mb4_0900_ai_ci'
                  ENGINE=InnoDB""", con)
    sql.execute("""CREATE TABLE `hw_4_3` (
                     `№` INT(10) NULL DEFAULT NULL,
                     `Месяц` DATE NULL DEFAULT NULL,
                     `Сумма платежа` FLOAT NULL DEFAULT NULL,
                     `Платеж по основному долгу` FLOAT NULL DEFAULT NULL,
                     `Платеж по процентам` FLOAT NULL DEFAULT NULL,
                     `Остаток долга` FLOAT NULL DEFAULT NULL,
                     `Проценты` FLOAT NULL DEFAULT NULL,
                     `Долг` FLOAT NULL DEFAULT NULL
                  )
                  COLLATE='utf8mb4_0900_ai_ci'
                  ENGINE=InnoDB""", con)
    df3 = pd.DataFrame()
    while index < 4:
         sheetName = f"Лист{index}"
         t_name = f"hw_4_{index}"
         print(sheetName)
         pdf = pd.read_excel("/Users/Xiaomi/Desktop/Geekbrains_ETL/s4_2.xlsx", sheet_name=sheetName)
         df = spark.createDataFrame(pdf)\
             .withColumn("Проценты", sum1(col("Платеж по процентам")).over(w))\
             .withColumn("Долг", sum1(col("Платеж по основному долгу")).over(w))
         df.show(5)
         df.write.format("jdbc").option("url", "jdbc:mysql://localhost:3306/spark?user=root&password=1q2w3e") \
            .option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", t_name) \
            .mode("append").save()
         index += 1
         df2 = df.toPandas()
         df3 = pd.concat([df3, df2], axis=1, ignore_index=True)
     
# Get current axis
    ax = plt.gca()
    ax.ticklabel_format(style='plain')
# bar plot
    df3.plot(kind='line',
             x=0,
             y=[6,7,14,15,22,23],
             ax=ax)
# set the title
    plt.title('Выплаты')
    ax.legend(["Проценты", "Долг", "Проценты120", "Долг120", "Проценты150", "Долг150"])
    plt.grid ( True )
    ax.set(xlabel=None)
# show the plot
plt.show()


spark.stop()
t1 = time.time()
print('finished', time.strftime('%H:%M:%S', time.gmtime(round(t1 - t0))))
