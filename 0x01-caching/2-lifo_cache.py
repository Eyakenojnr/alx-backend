#!/usr/bin/env python3
"""Implement LIFO cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a LIFO caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.order = [] # Track order of inserted keys

    def put(self, key, item):
        """Add an item into cache using LIFO strategy."""
        if key is None or item is None:
            return

        # Remove key if it already exists to update its position
        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        # If number of items in cache_data is more than BaseCaching.MAX_ITEMS
        #   - Discard the last item put in the cache
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
