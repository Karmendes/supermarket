from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from hook.hook_requests import call_api



default_args={
  'owner': 'karmendes',
  'start_date': datetime(2023,3,21),
  'email': ['lucas.mendes@play9.com.br'],
  'email_on_failure': True,
  'retries': 0,
  'retry_delay': timedelta(minutes=5),
  'execution_timeout': timedelta(minutes=30),
}

dag = DAG(
  'principal_dag',
  default_args=default_args,
  description='Pipeline responsavel pelo update dos preços',
  schedule_interval=None,
  dagrun_timeout=timedelta(minutes=60),
  catchup=False,
  tags=['api'],
)


task_zona_sul = PythonOperator(
    task_id='zona_sul_scrapping',
    python_callable=call_api,
    op_args=['zona_sul'],
    dag=dag
    )

task_prix = PythonOperator(
    task_id='prix_scrapping',
    python_callable=call_api,
    op_args=['prix'],
    dag=dag
    )

task_fake_1 = EmptyOperator(task_id='dbt_staging',dag=dag)

task_fake_2 = EmptyOperator(task_id='dbt_mart',dag=dag)

[task_zona_sul, task_prix] >> task_fake_1 >> task_fake_2