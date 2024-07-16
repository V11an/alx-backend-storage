#!/usr/bin/env python3
"""
List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    This function lists all documents in a pymongo collection.

    Args:
        mongo_collection: A pymongo collection object representing the collection to be queried.

    Returns:
        A list containing all documents in the collection or an empty list if there are no documents.
    """

    documents = list(mongo_collection.find({}))  # Find all documents with an empty query
    return documents
