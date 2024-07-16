#!/usr/bin/env python3
"""
Changing the school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update document with specific attribute: value
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
