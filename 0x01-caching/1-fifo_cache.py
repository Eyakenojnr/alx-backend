#!/usr/bin/env python3
"""Implements a FIFO cache."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines a FIFO caching system."""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Cache a key-item pair."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        # If number of items in cache_data is higher than BaseCaching.MAX_ITEMS
        #   - Discard first item put in cache
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None 
        return self.cache_data[key]
