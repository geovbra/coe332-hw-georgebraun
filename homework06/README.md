# Deploying a Flask App and Redis Database to a Kubernetes Cluster

## Overview

This folder contains instructions to deploy a containerized program that communicates with a redis database to a Kubernetes cluster and then interact with the program. The Flask application used for this is the same as the one in folder homework05.

## Script Explanation

The project consists of five YAML files and both the Dockerfile and the python script from the previous homework folder. Two of the YAML files are configurations for deploying the flask application, and the other three are for deploying the Redis database that the application uses to store data.

## Deploying the Program

First, deploy the three YAML files with "redis" in their name using the following command three times, replacing `example-file.yml` with the name of each file respectively (the order is not significant)

```
   kubectl apply -f example-file.yml
```

This creates a Deployment that keeps one Pod running a redis database open, a Service to easily interact with the redis pod, and a PersistentVolumeClaim (PVC) that the redis pod can permanently store its data in. 

Next, find the IP that the redis service is using by using the following command:

```
   kubectl describe service geovbra-test-redis-service
```

This will return some general data about the service, but we specifically want its IP:

```
   IP:                xx.xxx.xx.xxx # exact number of x's may vary
```

Take this IP and edit the `geovbra-test-flask-deployment.yml` file, replacing the old IP address in the `command` line with this one:

```
          command: ['sh', '-c', 'python app.py xx.xxx.xx.xxx']
```

This ensures that the flask container will be looking in the right place to interact with the redis database.

Finally, deploy the two YAML files with "flask" in their name using the same command as before (again, order doesn't matter):

```
   kubectl apply -f example-file.yml
```

This creates a Deployment that maintains two pods running the Flask application and a Service to interact with the pods.

## Interacting with ISS Data

To send requests to the API, we must first find the IP address that our container is using for Flask. This can be done with this command:

```
   kubectl describe service geovbra-test-flask-service
```

This will again return data on the service, and the following line has the IP address:

```
   IP:                yy.yyy.yy.yyy
```

Finally, to communicate with the service, we need to enter one of the two pods running the flask application. The names of the current running pods can be found with this command:

```
   kubectl get pods
```

This returns a list of pods, but copy the name of one of the pods with `flask` in its name.

To enter the pod, use the following command with the pod name:

```
   kubectl exec -it geovbra-test-flask-deployment-zzzzzzzzz-zzzzz -- /bin/bash
```

Now you should be able to interact with the data by using the `curl yy.yyy.yy.yyy:5000/<route here>` command inside the pod. There is only one route, `/data`, and this route can be sent a POST request (which loads and stores the meteorite data) and a GET request (which retrieves all of the meteorite data that was previously stored.

Sample commands and outputs:
```
[geovbra]$ curl 10.100.77.130:5000/data -X POST
Data loaded successfully
[geovbra]$ curl 10.100.77.130:5000/data
[
  {
    "GeoLocation": "(-75.6691, 60.6936)",
    "id": "10001",
    "mass (g)": "5754",
    "name": "Gerald",
    "recclass": "H4",
    "reclat": "-75.6691",
    "reclong": "60.6936"
  },
  {
    "GeoLocation": "(-9.4378, 49.5751)",
    "id": "10002",
    "mass (g)": "1701",
    "name": "Dominique",
    "recclass": "L6",
    "reclat": "-9.4378",
    "reclong": "49.5751"
  },
  ...
```
