#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end index for pagination"""
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page from the dataset"""
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        return data[start_index:end_index] if start_index < len(data) else []
