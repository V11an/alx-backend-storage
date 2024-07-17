#!/usr/bin/env python3
""" advanced task """


import requests
from functools import wraps
from datetime import timedelta
from cachetools import TTLCache


# Simple cache implementation with expiration using cachetools
cache = TTLCache(maxsize=100, ttl=timedelta(seconds=10))


def count_url_access(func):
    """Decorator to track URL access count."""

    @wraps(func)
    def wrapper(url):
        """Wraps the decorated function and updates the access count."""
        key = f"count:{url}"
        count = cache.get(key, 0)
        cache[key] = count + 1
        return func(url)

    return wrapper


# Improved get_page function with caching
@count_url_access
@cachetools.cachedmem(cache)
def get_page(url: str) -> str:
    """Retrieves the HTML content of a URL and caches the result.

    - Uses requests library to fetch the content.
    - Caches the result with an expiration time of 10 seconds.
    - Tracks the access count for each URL in a separate cache key.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    return response.text


# Example usage
url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))
print(f"URL '{url}' accessed {cache.get(f'count:{url}', 0)} times")
