#!/usr/bin/python3
"""Peak Finder Module

This module provides a function to find a peak in a list of unsorted integers.

Usage:
    from peak_finder import find_peak

    peak = find_peak(list_of_integers)
    print(f"The peak(s) in the list is/are: {peak}")

Note:
    There may be more than one peak in the list.

Algorithm Complexity:
    The function uses a binary search approach with O(log(n)) time complexity
    to find the peak(s).

Args:
    list_of_integers (list): A list of integers.

Returns:
    int or None: The peak(s) found in the list. Returns None if the list is empty.
"""
def find_peak(list_of_integers):
    list_ = list_of_integers

    # Return None if the list is empty
    if not list_:
        return None

    length = len(list_)
    start, end = 0, length - 1

    while start < end:
        mid = start + (end - start) // 2

        # Check if mid is a peak
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]

        # Adjust pointers based on the comparison with neighbors
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # Return the remaining element as a peak
    return list_[start]
