#!/usr/bin/env python3
import redis
import json
from flask import Flask, jsonify
import sys

app = Flask(__name__)

#with open(sys.argv[1], 'r') as redis_ip:
rd=redis.Redis(host=sys.argv[1], port=6379)

@app.route('/data', methods = ['GET'])
def data_post() -> str:
    """
    Communicates with redis container, returning meteorite landing data that was previously stored in a database.
    
    Returns:
        A formatted string representing a json list of meteorite data, or a string prompting the user to load data to
        the redis database if none exists.
    """
    if rd.get("ml_data") == None:
        return ("Please use this route with a post command to load data first\n")
    return jsonify(json.loads(rd.get("ml_data")))

@app.route('/data', methods = ['POST'])
def data_load() -> str:
    """
    Communicates with redis container, loading meteorite landing data and storing it in the redis database.
    
    Returns:
        A string notifying the user that the meteorite landing data has been successfully loaded and stored.
    """
    with open('ML_Data_Sample.json', 'r') as f:
        ml_data = json.load(f)
    
    rd.set("ml_data", json.dumps(ml_data["meteorite_landings"]))
    return "Data loaded successfully\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5005)
