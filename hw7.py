from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from pandas.io import sql
import warnings

warnings.filterwarnings("ignore")
con = create_engine("mysql://Airflow:1@localhost/spark")

sql.execute("""CREATE TABLE if not exists spark.`hw_7_temp` (
	`№` INT(10) NOT NULL AUTO_INCREMENT,
	`Город` TEXT NULL DEFAULT NULL,
	`Время` TIMESTAMP NULL DEFAULT NULL,
	`Температура` TEXT NULL DEFAULT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB""", con)


def temp_sql(city, temp):
    dt_now = datetime.now()
    df = pd.DataFrame()
    df
    df.to_sql("hw_7_temp", con, if_exists='append')
