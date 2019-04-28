#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/2/17 19:25
"""

list_order = [7, 4, 3, 67, 34, 1, 8]


def bubble_sort(arr):
    """
    sort the data with bubble sort algorithm.
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


bubble_sort(list_order)
print(list_order)
