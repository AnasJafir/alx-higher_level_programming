#!/usr/bin/python3
"""Peak Module"""
def find_peak(list_of_integers):
    """Method to find the peak of a list"""
    lst = list_of_integers
    if lst == []:
        return None
    left, right = 0, len(lst) - 1
    while left < right:
        mid = left + (right - left) // 2
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]
        if lst[mid - 1] > lst[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return lst[left]
