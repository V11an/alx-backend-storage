#!/usr/bin/env python3
"""
task_11 'where can I learn Python'
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find a topic by specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
