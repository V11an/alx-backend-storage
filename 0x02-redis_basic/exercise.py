#!/usr/bin/env python3
"""
task_1
"""


from uuid import uuid4
from typing import Union
import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()  # Connect to Redis and store as private variable
        self._redis.flushdb()  # Flush existing data from Redis

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns the generated key.

        Args:
            data: The data to be cached (str, bytes, int, or float).

        Returns:
            A string representing the randomly generated key.
        """
        key = str(uuid4())  # Generate a random key using uuid4
        self._redis.set(key, data)  # Store data in Redis with the key
        return key
