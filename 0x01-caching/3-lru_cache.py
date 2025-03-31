#!/usr/bin/env python3
"""LRU cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements the LRU caching system."""

    def __init__(self):
        super().__init__()
        self.order = []  # Track the order of access

    def put(self, key, item):
        """Add an item to the cache using LRU strategy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)  # Remove key to update its position

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)  # Remove the least recently used key
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move key to the end of the list to mark it as recently used
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
