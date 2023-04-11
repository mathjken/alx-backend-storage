#!/usr/bin/env python3
"""
ouputs status about Nginx logs?
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    num = nginx_collection.count()
    num_get = nginx_collection.find({"method": "GET"}).count()
    num_post = nginx_collection.find({"method": "POST"}).count()
    num_put = nginx_collection.find({"method": "PUT"}).count()
    nu_patch = nginx_collection.find({"method": "PATCH"}).count()
    num_delete = nginx_collection.find({"method": "DELETE"}).count()
    num_status = nginx_collection.find(
        {"method": "GET", "path": "/status"}).count()

    print("{} logs".format(num))
    print("Methods:")
    print("\tmethod GET: {}".format(num_get))
    print("\tmethod POST: {}".format(num_post))
    print("\tmethod PUT: {}".format(num_put))
    print("\tmethod PATCH: {}".format(num_patch))
    print("\tmethod DELETE: {}".format(num_delete))
    print("{} status check".format(num_status))
