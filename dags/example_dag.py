# dags/example_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    "example_dag", schedule_interval="@daily", default_args=default_args, catchup=False
) as dag:
    print_date = BashOperator(task_id="print_date", bash_command="date")
