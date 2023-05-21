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

In this project we are going to create Cloud Composer environment and deploy DAG which contains creating container for Dataproc, 
running pipeline and shutting down container. This solution also will check if this is first time when you run pipeline for given date or it is second time - then deleting data is executed.



<img width="1275" alt="Zrzut ekranu 2023-05-15 o 13 01 18" src="https://github.com/eda6767/airflow/assets/102791467/a4aea114-af3a-4dbe-80c4-661ca03ba420">



<img width="689" alt="Zrzut ekranu 2023-05-15 o 13 02 11" src="https://github.com/eda6767/airflow/assets/102791467/a0574b3d-8478-4c6e-903b-a0081ca981b2">


<img width="1428" alt="Zrzut ekranu 2023-05-15 o 13 02 47" src="https://github.com/eda6767/airflow/assets/102791467/c7c00d7e-487e-4493-aa85-639726f92d5e">



<img width="1428" alt="Zrzut ekranu 2023-05-15 o 22 07 41" src="https://github.com/eda6767/airflow/assets/102791467/8c9ed6a1-7ec3-4b48-a03d-4605a27fff6d">





