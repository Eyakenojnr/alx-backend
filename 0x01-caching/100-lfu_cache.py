#!/usr/bin/env python3
"""LFU Cache"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Implements the LFU caching system."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.freq_count = {}  # Store usage frequency
        self.lfu_order = OrderedDict()  # OrderedDict to maintain LRU order wihtin same frequency

    def put(self, key, item):
        """Assign key-value pair to cache_data and handle LFU eviction."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_count[key] += 1  # Increase frequency count
            self.lfu_order.move_to_end(key)  # Maintain LRU order
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used keys
                min_freq = min(self.freq_count.values())
                lfu_keys = [k for k, v in self.freq_count.items() if v == min_freq]

                # If multiple keys have same frequency, use LRU evict
                if len(lfu_keys) > 1:
                    for k in self.lfu_order.keys():
                        if k in lfu_keys:
                            discarded_key = k
                            break
                else:
                    discarded_key = lfu_keys[0]

                del self.cache_data[discarded_key]
                del self.freq_count[discarded_key]
                del self.lfu_order[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.freq_count[key] = 1
            self.lfu_order[key] = None   # Add to LRU order

    def get(self, key):
        """Retrieve item from cache_data and update its usage frequency"""
        if key is None or key not in self.cache_data:
            return None

        self.freq_count[key] += 1
        self.lfu_order.move_to_end(key)  # Update LRU order
        return self.cache_data[key]
