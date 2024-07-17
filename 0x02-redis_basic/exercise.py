#!/usr/bin/env python3
"""
task_1
"""


from uuid import uuid4
import redis
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wraps the decorated function and returns the wrapper."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wraps the decorated function and returns the wrapper."""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


class Cache:
    """Declares a Cache redis class."""

    def __init__(self):
        """Upon initialization, stores an instance and flushes."""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string."""
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Converts the data back to the desired format.

        If no conversion function (fn) is provided, returns the raw bytes.
        """
        value = self._redis.get(key)
        if value is None:
            # Key doesn't exist, return None as per original behavior
            return None
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """Parametrizes Cache.get with the correct conversion function (decode)."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Parametrizes Cache.get with the correct conversion function (int)."""
        # Handle potential conversion errors gracefully
        value = self.get(key, fn=lambda d: int(d.decode("utf-8")))
        if isinstance(value, Exception):
            raise value  # Re-raise the conversion exception
        return value
