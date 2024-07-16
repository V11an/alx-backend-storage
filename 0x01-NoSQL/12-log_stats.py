#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient

# Database and collection names (modify if needed)
DATABASE_NAME = "logs"
COLLECTION_NAME = "nginx"

# HTTP methods to count
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Path for status check
STATUS_CHECK_PATH = "/status"


def connect_to_mongo():
  """
  Connects to the MongoDB server using the configured database and collection.

  Returns:
      A pymongo MongoClient object.
  """
  client = MongoClient()
  db = client[DATABASE_NAME]
  collection = db[COLLECTION_NAME]
  return collection


def count_documents():
  """
  Counts the total number of documents in the collection.

  Returns:
      The number of documents as an integer.
  """
  collection = connect_to_mongo()
  count = collection.count_documents({})
  return count


def count_documents_by_method():
  """
  Counts the number of documents for each HTTP method in the METHODS list.

  Returns:
      A dictionary with method names as keys and counts as values.
  """
  collection = connect_to_mongo()
  method_counts = {}
  for method in METHODS:
    query = {"method": method}
    count = collection.count_documents(query)
    method_counts[method] = count
  return method_counts


def count_status_checks():
  """
  Counts the number of documents with the specified path for status checks.

  Returns:
      The number of documents with the status check path as an integer.
  """
  collection = connect_to_mongo()
  query = {"path": STATUS_CHECK_PATH}
  count = collection.count_documents(query)
  return count


def main():
  """
  Main function to execute the script and display statistics.
  """
  total_documents = count_documents()
  method_counts = count_documents_by_method()
  status_checks = count_status_checks()

  print(f"{total_documents} logs")
  print("Methods:")
  for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
  print(f"{status_checks} status check")


if __name__ == "__main__":
  main()
