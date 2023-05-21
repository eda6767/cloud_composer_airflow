# Apache Airflow


```
python3 --version
python3 -m venv py_env
source py_env/bin/activate

https://github.com/apache/airflow 
pip install 'apache-airflow==2.6.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.0/constraints-3.10.txt
 
 export AIRFLOW_HOME=.
 airflow db init
 airflow webserver -p 8080
 
 export AIRFLOW_HOME=~/airflow
 airflow webserver -p 8080
 
 airflow users create --username admin --firstname firstname --lastname lastname --role Admin --email admin@domain.com
 

```
 


# Apache Airflow - Cloud Composer on GCP

######  In this project we are going to create Cloud Composer environment and deploy DAG which contains creating container for Dataproc, running pipeline and shutting down container. This solution also will check if this is the first time when you run pipeline for given date or it is second time - then deleting data is executed.




<img width="1275" alt="Zrzut ekranu 2023-05-15 o 13 01 18" src="https://github.com/eda6767/airflow/assets/102791467/a4aea114-af3a-4dbe-80c4-661ca03ba420">


######  As a first step we will create Composer Environment. For this purpose we will set the minimum number of nodes which is - 3, and n1-stanard-1 as a machine type.


<img width="689" alt="Zrzut ekranu 2023-05-15 o 13 02 11" src="https://github.com/eda6767/airflow/assets/102791467/a0574b3d-8478-4c6e-903b-a0081ca981b2">


###### After as environments has been created we can check DAG list, logs, DAG folder and also Aifrlow webserver. 

<br>


<img width="1428" alt="Zrzut ekranu 2023-05-15 o 13 02 47" src="https://github.com/eda6767/airflow/assets/102791467/c7c00d7e-487e-4493-aa85-639726f92d5e">

<br>

###### Now, we have to define first DAG. For this purpose we have to copy python file to DAG folder. This can be done throught console  or throught cloud shell. :shipit: 

<br><img width="1374" alt="Zrzut ekranu 2023-05-21 o 20 30 23 kopia" src="https://github.com/eda6767/airflow/assets/102791467/06cb2330-ba95-445d-855c-1cb53ef0605d">


##### After defining first dag, we are able to view a diagram in DAG list, in diagram section. We have first task, which starts pipeline containing DummyOperator. Next we are using branching which will check if there is the first running pipeline, or second, what means that we need to delete data from partition on BigQuery destination table. After this DAG creates cluster with given parameters, runs main ETL pipeline, and then deletes dataproc cluster.



<br>

<img width="1428" alt="Zrzut ekranu 2023-05-15 o 22 07 41" src="https://github.com/eda6767/airflow/assets/102791467/8c9ed6a1-7ec3-4b48-a03d-4605a27fff6d">




```
[2023-05-15T18:14:19.205+0000] {taskinstance.py:1402} INFO - Marking task as FAILED. dag_id=PROCEDURE, task_id=branching, execution_date=20230513T000000, start_date=20230515T181417, end_date=20230515T181419
[2023-05-15T18:14:19.236+0000] {standard_task_runner.py:100} ERROR - Failed to execute job 7 for task branching (403 POST https://bigquery.googleapis.com/bigquery/v2/projects/clean-sylph-377411/jobs?prettyPrint=false: Access Denied: Project clean-sylph-377411: User does not have bigquery.jobs.create permission in project clean-sylph-377411.
```


