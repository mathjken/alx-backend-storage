#!/usr/bin/env python3
'''School that has specific topics
'''


def schools_by_topic(mongo_collection, topic):
    '''Gets the list of school having a specific topic.
    '''
    output = {"topics":  {"$in": [topic]}}
    return mongo_collection.find(output)
