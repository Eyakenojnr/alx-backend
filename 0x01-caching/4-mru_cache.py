#!/usr/bin/env python3
"""MRU cache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements the MRCU caching system."""

    def __init__(self):
        """Initialize class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop(-2)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Retrieve an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
