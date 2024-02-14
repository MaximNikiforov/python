import os
import requests
import pendulum
import pandas as pd
import tabulate
from datetime import datetime, timedelta
from sqlalchemy import inspect,create_engine
from pandas.io import sql
from airflow.decorators import dag, task
from airflow.providers.telegram.operators.telegram import TelegramOperator

os.environ["no_proxy"]="*"

@dag(
    dag_id="wether-tlegram",
    schedule="@once",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
)

def WetherETL():

    send_message_telegram_task = TelegramOperator(
        task_id='send_message_telegram',
        telegram_conn_id='telegram_default',
        token='5880568196:AAHVCp2d5Sdq62N9hVQFBd9WlZARkFRo8NQ',
        chat_id='360293860',
        text='Wether in Moscow \nYandex: ' + "{{ ti.xcom_pull(task_ids=['yandex_wether'],key='wether')[0]}}" + " degrees" +
        "\nOpen wether: " + "{{ ti.xcom_pull(task_ids=['open_wether'],key='open_wether')[0]}}" + " degrees",
    )

    @task(task_id='yandex_wether')
    def get_yandex_wether(**kwargs):
        ti = kwargs['ti']
        url = "https://api.weather.yandex.ru/v2/informers/?lat=55.75396&lon=37.620393"

        payload={}
        headers = {
        'X-Yandex-API-Key': '33f45b91-bcd4-46e4-adc2-33cfdbbdd88e'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print("test")
        a=response.json()['fact']['temp']
        print(a)
        ti.xcom_push(key='wether', value=response.json()['fact']['temp'])
#        return str(a)
    @task(task_id='open_wether')
    def get_open_wether(**kwargs):
        ti = kwargs['ti']
        url = "https://api.openweathermap.org/data/2.5/weather?lat=55.749013596652574&lon=37.61622153253021&appid=2cd78e55c423fc81cebc1487134a6300"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print("test")
        a=round(float(response.json()['main']['temp']) - 273.15, 2)
        print(a)
        ti.xcom_push(key='open_wether', value=round(float(response.json()['main']['temp']) - 273.15, 2))
#        return str(a)
    @task(task_id='python_wether')
    def get_wether(**kwargs):
        print("Yandex "+str(kwargs['ti'].xcom_pull(task_ids=['yandex_wether'],key='wether')[0])+" Open "+str(kwargs['ti'].xcom_pull(task_ids=['open_wether'],key='open_wether')[0]))
    
    @task(task_id='temp_sql')
    def temp_sql(**kwargs):
        ti = kwargs['ti']
        con = create_engine("mysql://Airflow:1@localhost/spark")
        temp_yandex = kwargs['ti'].xcom_pull(task_ids=['yandex_wether'],key='wether')[0]
        temp_open = kwargs['ti'].xcom_pull(task_ids=['open_wether'],key='open_wether')[0]
        dt_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df = pd.DataFrame({"Время": [dt_now], "Яндекс": [temp_yandex], "Опен": [temp_open]})
        df.to_sql("hw_8_temp", con, if_exists='append', index=False)
    
    @task(task_id='hw_4_credit')        
    def hw_4_credit(**kwargs):
        ti = kwargs['ti']
        con = create_engine("mysql://Airflow:1@localhost/spark")
        df1 = pd.read_sql_table('hw_4_1', con)            
        ti.xcom_push(key='text', value=df1.head(20).to_markdown())
    
    send_message_2_telegram_task = TelegramOperator(
        task_id='send_message_2_telegram',
        telegram_conn_id='telegram_default',
        token='5880568196:AAHVCp2d5Sdq62N9hVQFBd9WlZARkFRo8NQ',
        chat_id='360293860',
        text="{{ti.xcom_pull(task_ids=['hw_4_credit'],key='text')[0]}}",
    )    
            
    get_yandex_wether() >> get_open_wether() >> get_wether() >> temp_sql() >> send_message_telegram_task
    hw_4_credit() >> send_message_2_telegram_task

dag = WetherETL()
