# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080//ui/
```

Your Swagger definition lives here:

```
http://localhost:8080//swagger.json
```
Authentication
```
To access the endpoints requiring authorization make an .env file and initialize SECRET
eg: SECRET=secret
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:
```
#build docker-compose
docker-compose build

#start docker-compose
docker-compose start -d

```

## Running with Kubernetes

To run the server on Kubernetes container, please execute the following from the root directory:
```
#start minikube
-minikube start

#Launch pods
-kubectl apply -k k8s

#check if pods are running
-kubectl get pods

#Configure and initialize Mongo replicaSet
-kubectl exec -it mongo-0 /bin/bash
-mongo -u root2 -p root2

#inside the mongo shell
-rs.initiate();
-var cfg = rs.conf();
-cfg.members[0].host="mongo-0.mongo:27017";
-rs.reconfig(cfg);
-rs.add("mongo-1.mongo:27017");
-rs.add("mongo-2.mongo:27017");

#in another terminal window expose the server
-sudo minikube tunnel

#now you can access it on localhost:8080/ui
```
