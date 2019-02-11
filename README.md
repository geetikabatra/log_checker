# log_checker

Log checker is a log tracking system which monitors HTTP traffic present in access.log. Log data conforms to [HTTP standards](https://www.w3.org/Daemon/User/Config/Logging.html).

The system is a scalable and distributed system. It uses docker which can be used to scale horizontally.

There are three docker services.

### schedule-server
It is a flask service which is used to create request and in turn dump data into the log. The app uses [swagger](https://swagger.io/) which is used for modeling cleaner api and documentation. 
It provides a UI interface to access api endpoints. It is available on endpoint 
```
http://localhost:5000/api/v1/ui/
```
image:images/swagger.png[title="swagger", alt="swagger"]

### scheduler
It is a job which is scheduled every 2 minutes and checks the log file `/var/log/access.log` for any activity which might need to be noticed.

### locust-server
A testing server which throws multiple requests to load test the app. It uses [locust.io](https://locust.io/).
It is available on the endpoint 
```
http://localhost:8089/
```
image:images/locust.png[title="locust", alt="locust"]


Steps to build the service and run.

clone the repository.
```
git clone https://github.com/GeetikaBatra/log_checker.git
```
For initial setup, Makefile is present. It contains the follwing options 
###
make clean:
Removes the tmp folder.

###
make genrate
Creats the tmp/access.log . This file is mounted to scheduler and schedule-server

###
make docker
Builds and Runs docker-compose

Make sure you have docker and docker-compose=>3.5 available in your system. Run
```
make all
```

To separately build the docker-compose.
Run 
```
docker-compose build
```

To run all the services.
```
docker-compose up
```
