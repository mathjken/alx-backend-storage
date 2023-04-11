#!/usr/bin/env python3
"""get all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all documents in a collection
    """
    
    documents = mongo_collection.find()
    return [doc for doc in documents]
