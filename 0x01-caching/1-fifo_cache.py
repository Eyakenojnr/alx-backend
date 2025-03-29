#!/usr/bin/env python3
"""Implements a FIFO cache."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines a FIFO caching system."""

    def __init__(self):
        super().__init__()
        self.order = []  # Track order of inserted keys

    def put(self, key, item):
        """Cache a key-item pair."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        # If number of items in cache_data is higher than BaseCaching.MAX_ITEMS
        #   - Discard first item put in cache
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)  # Remove first inserted key
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
