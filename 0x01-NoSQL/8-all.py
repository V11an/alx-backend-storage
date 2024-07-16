#!/usr/bin/env python3
"""
Lists all documents in Python3
"""
import pymongo


def list_all(mongo_collection):
    """
    a func to list all doc in collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
