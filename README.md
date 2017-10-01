# Sample Web Scraping using Scrapy for AJAX websites

This project is a sample project for scraping data from ajax websites using scrapy.
The scraping job is set to run daily to get the products information from e-commerce sites.
The scheduling for scraping is using airbnb's airflow
The websites we used are zalora.co.id and berrybenka.com.

## Getting Started

Just clone this project and run build.sh command
```
./build.sh
```

Once the project is built, to open airflow admin page. use the browser to go to:

```
http://localhost:8081
```
Then, start the scraping process by switching to "ON" for the starter_dag on the airflow's admin page.
The results are stored in files located in volume called data for csv files, and volume called images and images of the products.

To access the data once the scraping process is done, run the following command on terminal:

```
docker-compose exec scraper /bin/bash
cd /data
cd /images
```

To uninstall or clean all installation made before just run clear-all.sh
```
./clear-all.sh
```

### Prerequisites

OS: Linux (if possible), other OS as long as it supports docker and docker-compose
Container: docker and docker-compose

To install docker: https://docs.docker.com/engine/installation/
To install docker-compose: https://docs.docker.com/compose/install/

### Installing

Just run build.sh

```
./build.sh
```

## Authors

* **Rahadian Bayu Permadi (rahadian.bayu.permadi@gmail.com)**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
