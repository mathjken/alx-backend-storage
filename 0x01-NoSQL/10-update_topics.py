#!/usr/bin/env python3
"""
Change school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates all  topics of a document in a collection
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
