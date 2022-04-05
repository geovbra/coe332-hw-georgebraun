# Storing and Retrieving Meteorite Landing Data in a Redis Database

## Overview

This folder contains instructions and resources to access and use a containerized program that communicates with a redis container to store and retrieve data recorded from meteorite landing sites. The data used in this program can be found here:

https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

## Script Explanation

The project consists of one python scripts and a JSON file of sample data. The first python script, app.py, sets up a REST API using Flask along with one route.

## Requirements

To use this container, you have to first pull it from Docker. Simply enter the following command into the terminal:

```
   docker pull geovbra/redis_ml_data_analysis:1.0
```

This retrieves the container image from DockerHub and allows you to begin running the program.

Alternatively, you can run the `Dockerfile` included in this folder to build an image yourself, provided you have the python script in the same repository:

```
   docker build -t geovbra/redis_ml_data_analysis:1.0 .
```

This container also communicates with a Redis container, which manages a local database. To ensure this container runs properly, run an instance of redis using the following commmand:

```
   docker run -v $(pwd)/data:/data -d -p 6405:6379 --name=geovbra-redis redis:6 --save 1 1
```

This command mounts the `data` folder in the current directory inside the redis container, allowing any stored data to persist when the redis container is stopped or restarted. The redis container will also save the data to a single backup file once every second.

## Running the Program

Once you have started the redis container and pulled/built the docker image, use the following command:

```
   docker inspect geovbra-redis | grep IPAddress
```

This should return the redis container's ID, which will allow this container to communicate with the redis container:

```
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.0",
                    "IPAddress": "172.17.0.0",
```

Here, your IP address may be different from the sample address.

To run this container, use the following command:

```
   docker run --rm -d geovbra/redis_ml_data_analysis:1.0 --name=geovbra-ml-redis app.py 172.17.0.0
```

Be sure to replace the sample IP address at the end of this command with the IP address from the previous step.

## Interacting with ISS Data

To send requests to the API, we must first find the IP address that our container is using for Flask. This can be done with this command:

```
   docker logs geovbra-ml-redis
```

This will return a a large amount of information, but the following line has the IP address:

```
 * Running on http://172.17.0.0:5005 (Press CTRL+C to quit)
```

Note that there are two IP addresses in the information returned by docker logs, so be sure to use the line containing ```(Press CTRL+C to quit)```, which is the second IP address line.

To interact with the data, use the `curl 172.17.0.0:5005/<route here>` command, where the sample IP address is replaced by the one found in the previous step. There is only one route, `/data`, and this route can be sent a POST request (which loads and stores the meteorite data) and a GET request (which retrieves all of the meteorite data that was previously stored.

Sample commands and outputs:
```
[geovbra]$ curl 172.17.0.0:5005/data -X POST
Data loaded successfully
[geovbra]$ curl 172.17.0.0:5005/data
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