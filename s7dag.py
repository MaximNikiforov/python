from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
import pendulum
import requests
import pandas as pd
import pyspark,time,platform,sys,os
from datetime import datetime
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col,lit,current_timestamp
import matplotlib.pyplot as plt
from sqlalchemy import inspect,create_engine
from pandas.io import sql
import warnings,matplotlib
from pyspark.sql.window import Window
from pyspark.sql.functions import sum as sum1

default_args = {
'owner': 'AGanshin',
'depends_on_past': False,
'start_date': pendulum.datetime(year=2022, month=6, day=1).in_timezone('Europe/Moscow'),
'email': ['alex@alex.ru'],
'email_on_failure': False,
'email_on_retry': False,
'retries': 0,
'retry_delay': timedelta(minutes=5)
}
#DAG1
dag1 = DAG('AGanshin001',
default_args=default_args,
description="seminar_6",
catchup=False,
schedule_interval='0 6 * * *')
task1 = BashOperator(
task_id='pyspark',
bash_command='export SPARK_HOME=/home/spark && export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin && python3 /home/modolock/s6.py',
dag=dag1)
task2 = BashOperator(
task_id='spark',
bash_command='export SPARK_HOME=/home/spark && export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin && spark-shell -i /home/modolock/s6s1.scala',
dag=dag1)
task2 >> task1
#DAG3
from airflow.operators.python import PythonOperator
import pandas as pd
from sqlalchemy import inspect,create_engine
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pandas.io import sql
import time
#pip install openpyxl
dag3 = DAG('AGanshin003',
default_args=default_args,
description="seminar_6",
catchup=False,
schedule_interval='0 8 * * *')
def hello(**kwargs):
  encoding="ISO-8859-1"
  print('Hello from {kw}'.format(kw=kwargs['my_keyword']))
  df=5+5
  print(df)
  df=pd.read_excel('/home/modolock/s4_2.xlsx')
  con=create_engine("mysql://Airflow:1@localhost:33061/spark")
  print(df)
  df['долг'] = df['Платеж по основному долгу'].cumsum()
  df['проценты'] = df['Платеж по процентам'].cumsum()
  df.to_sql('credit',con,schema='spark',if_exists='replace',index=False)
t2 = PythonOperator(
task_id='python3',
dag=dag3,
python_callable=hello,
op_kwargs={'my_keyword': 'Airflow 1234'}
)
dag11 = DAG( 'hello_world' , description= 'Hello World DAG' , 
          schedule_interval= '0 12 * * *' , 
          start_date=datetime( 2023 , 1 , 1
          ), catchup= False ) 

hello_operator = BashOperator(task_id= 'hello_task' , bash_command='echo Hello from Airflow', dag=dag11)
hello_file_operator = BashOperator(task_id= 'hello_file_task' , bash_command='sh /home/modolock/s6.sh ', dag=dag11) 
skipp_operator = BashOperator(task_id= 'skip_task' , bash_command='exit 99', dag=dag11) 

hello_operator >> hello_file_operator >> skipp_operator

def print_hello (): 
    return 'Hello world from Airflow DAG!' 

def skipp():
    return 99
dag22 = DAG( 'hello_world1' , description= 'Hello World DAG' , 
          schedule_interval= '0 12 * * *' , 
          start_date=datetime( 2023 , 1 , 1
          ), catchup= False ) 

hello_operator2 = PythonOperator(task_id= 'hello_task2' , python_callable=print_hello, dag=dag22)
skipp_operator2 = PythonOperator(task_id= 'skip_task2' , python_callable=skipp, dag=dag22)
hello_file_operator2 = BashOperator(task_id= 'hello_file_task2' , bash_command='python3.8 /home/alex/s6t2.py', dag=dag22)
hello_operator2 >> skipp_operator2 >> hello_file_operator2
###############################
def hw_7_get_temp(**kwargs):

    ti = kwargs['ti']

    city = "Moscow"

    api_key = "9e09ab59b55473a15edd2c94a4dba25c"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    payload = {}

    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # ti.xcom_push(key='hw_7_open_weather', value=round(float(response.json()['main']['temp'])-273.15, 2)

    return round(float(response.json()['main']['temp'])-273.15, 2)


def hw_7_check_temp(ti):

    temp = int(ti.xcom_pull(task_ids='hw_7_get_temperature_task'))

    print(f'Temperature now is {temp}')

    if temp >= 15:

        return 'hw_7_print_warm'

    else:

        return 'hw_7_print_cold'

def temp_sql(ti):

    con=create_engine("mysql://Airflow:1@localhost/spark")

    city = "Moscow"

    temp = int(ti.xcom_pull(task_ids='hw_7_get_temperature_task'))

    dt_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    df = pd.DataFrame({"Город": [city], "Время": [dt_now], "Температура": [temp]})
    
    df.to_sql("hw_7_temp", con, if_exists='append', index=False)
    
    return df.head()
    
def plot_4():

    con = create_engine("mysql://Airflow:1@localhost/spark")
    df1 = pd.read_sql_table('hw_4_1', con)
    df2 = pd.read_sql_table('hw_4_2', con)
    df3 = pd.read_sql_table('hw_4_3', con)
    df4 = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
    # Get current axis
    ax = plt.gca()
    ax.ticklabel_format(style='plain')
# bar plot
    df4.plot(kind='line',
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
    plt.savefig('4.png')
    return "4.png saved"

with DAG(

        'hw_7_weather_check_warm_or_cold',

        start_date=datetime(2024, 1, 1),

        catchup=False,

        tags=['homework_ETL'],

) as dag:

    plot_4_task = PythonOperator(

        task_id='plot_4_task',

        python_callable=plot_4,

    )

    hw_7_get_temperature_task = PythonOperator(

        task_id='hw_7_get_temperature_task',

        python_callable=hw_7_get_temp,

    )
    
    temp_sql_task = PythonOperator(

        task_id='temp_sql_task',

        python_callable=temp_sql,

    )

    hw_7_check_temperature_task = BranchPythonOperator(

        task_id='hw_7_check_temperature_task',

        python_callable=hw_7_check_temp,

    )

    hw_7_print_warm = BashOperator(

        task_id='hw_7_print_warm',

        bash_command='echo "It is warm"',

    )

    hw_7_print_cold = BashOperator(

        task_id='hw_7_print_cold',

        bash_command='echo "It is cold"',

    )

    hw_7_get_temperature_task >> temp_sql_task >> hw_7_check_temperature_task >> [
        hw_7_print_warm, hw_7_print_cold]
