#!/bin/bash

docker-compose stop
docker-compose down
docker rmi scrapysplash_scraper
docker volume rm $(docker volume ls -f dangling=true -q)
