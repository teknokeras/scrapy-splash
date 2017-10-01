from datetime import datetime, timedelta
import json

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.sensors import HttpSensor
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner': 'Rahadian Bayu Permadi',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['rahadian.bayu.permadi@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('starter_dag',
    default_args=default_args, schedule_interval='@daily')

berrybenka = BashOperator(
    task_id='scrape_berrybenka_starter',
    bash_command='python /code/crawler/spiders/berrybenka/__init__.py',
    retries=3,
    dag=dag)

zalora = BashOperator(
    task_id='scrape_zalora_starter',
    bash_command='python /code/crawler/spiders/zalora/__init__.py',
    retries=3,
    dag=dag)

zalora.set_upstream(berrybenka)
