#!/bin/bash

docker-compose up -d --build
docker-compose exec scraper airflow scheduler &
