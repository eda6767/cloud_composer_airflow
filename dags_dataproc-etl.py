# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:44:02 2023

"""
from datetime import timedelta, datetime
from airflow import DAG 
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocDeleteClusterOperator,
    DataprocSubmitJobOperator,
    ClusterGenerator)
from airflow.providers.google.cloud.sensors.dataproc import DataprocJobSensor
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

GOOGLE_CONN_ID = "google_cloud_default"
PROJECT_ID="clean-sylph-377411"
BUCKET_NAME = 'dataproc_mcc_proc'
CLUSTER_NAME = 'dataproc-cluster'
REGION = 'europe-west1'
PYSPARK_URI = 'gs://dataproc_mcc_proc/dataproc.py'

PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": PYSPARK_URI},
}

CLUSTER_CONFIG = ClusterGenerator(
    project_id=PROJECT_ID,
    zone="europe-west1-b",
    master_machine_type="n1-standard-2",
    worker_machine_type="n1-standard-2",
    num_workers=2,
    worker_disk_size=500,
    master_disk_size=500,
    storage_bucket=BUCKET_NAME,
).make()

default_args = {
    'owner': 'DAR',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'start_date':  days_ago(2),
    'retry_delay': timedelta(minutes=5),
}


with DAG('MCC_PROCEDURE', schedule_interval='@once', default_args=default_args) as dag:
    start_pipeline = DummyOperator(
        task_id = 'start_pipeline',
        dag = dag
        )
    create_cluster = DataprocCreateClusterOperator(
        task_id="create_cluster",
        project_id=PROJECT_ID,
        cluster_config=CLUSTER_CONFIG,
        region=REGION,
        cluster_name=CLUSTER_NAME,
    )
    pyspark_task = DataprocSubmitJobOperator(
        task_id="pyspark_task", 
        job=PYSPARK_JOB, 
        region=REGION, 
        project_id=PROJECT_ID,
    )
    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster", 
        project_id=PROJECT_ID, 
        cluster_name=CLUSTER_NAME, 
        region=REGION,
    )
    finish_pipeline = DummyOperator(
        task_id = 'finish_pipeline',
        dag = dag
    )

start_pipeline >> create_cluster >> pyspark_task >> delete_cluster >> finish_pipeline