from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import requests
import os
from datetime import timezone, timedelta
import joblib
import pendulum

#========================Task Definition=========================
def create_txt_file():
    with open('./example.txt', 'w') as f:
        f.write("Hello, Airflow!\n")
        f.write("This is a sample text file.\n")

#=========================DAG Definition=========================
with DAG(
    dag_id='ml_pipeline_example',
    schedule='0 0 * * *',  # 매일 자정 실행
    start_date=pendulum.datetime(2023,10,15, tz="Asia/Seoul"),
    catchup=False,
    tags=["ex","ex2"],
) as dag:
    ex_bash_t1 = BashOperator(
        task_id="ex_bash_t1",
        bash_command="echo $HOSTNAME",
    )

    ex_python_t2 = PythonOperator(
        task_id="ex_python_t2",
        python_callable=create_txt_file,
    )

    ex_bash_t1 >> ex_python_t2