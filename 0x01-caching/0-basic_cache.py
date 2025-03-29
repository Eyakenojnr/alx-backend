#!/usr/bin/env python3
"""Basic cache."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements a Basic Cache
    """

    def put(self, key, item):
        """Add an item to cache."""
        if key != None or item != None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
