# dags/example_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def log_message():
    print("DAG created, wuhhuuu")


default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    "example_dag", schedule_interval="@daily", default_args=default_args, catchup=False
) as dag:
    log_task = PythonOperator(task_id="log_message", python_callable=log_message)
    print_date = BashOperator(task_id="print_date", bash_command="date")

    log_task >> print_date
