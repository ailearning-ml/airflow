from airflow import dag
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'datamasterlab',
    'start_date': datetime(year:2024,month:10,day:22),
    'catchup':False
} 


dag = DAG(
        dag_id: 'hello_world'.
        default_args = default_args,
        schedule=timedelta(days=1)
)

t1 = BashOperator(
   task_id = 'hello_world',
   bash_command='echo "Hello World"',
   dag=dag
)    

t2 = BashOperator(
   task_id = 'hello_dml',
   bash_command='echo "Hello DAta MAstery Lab"',
   dag=dag
)

t1 >> t2

