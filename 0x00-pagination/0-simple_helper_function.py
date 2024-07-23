#!/usr/bin/env python3
"""
Module containing a simple helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
     Function to calculate the start and end index for a given page and page size.

     Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
