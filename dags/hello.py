from airflow import dag
from airflow.operators.bash import BashOperator
from datetime import datetime as dt, timedelta

default_args = {
    'owner': 'datamasterlab',
    'start_date': dt.datetime(2024,10,22),
    'catchup':False
} 


dag = DAG(
        dag_id="hello_world",
        default_args = default_args,
        schedule=timedelta(days=1)
)

t1 = BashOperator(
   task_id ='hello_world',
   bash_command='echo "Hello World"',
   dag=dag
)    

t2 = BashOperator(
   task_id ='hello_dml',
   bash_command='echo "Hello DAta MAstery Lab"',
   dag=dag
)

t1 >> t2

