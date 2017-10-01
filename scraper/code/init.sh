#!/bin/bash

rm airflow_home/airflow.db
rm airflow_home/airflow-webserver.pid
rm -rf airflow_home/logs
airflow version
airflow initdb
airflow webserver 
