#!/usr/bin/python3
"""This function finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    li = list_of_integers
    l = len(li)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != l - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
