#!/usr/bin/env python3
"""
Insert document in Python3
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert documents into collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
