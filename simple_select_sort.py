#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/1/18 11:52
"""


def simple_select_sort(arr):
    """
    sorted the data with simple select sort algorithm.

    :param arr: the name of the list.
    :return: the new list which has been sorted from small number to big number.
    """
    for i in range(len(arr)-1):
        k = i
        for j in range(k+1,len(arr)):
            if arr[k] > arr[j]:
                k = j
        if k != i:
            swap(arr, k, i)


def swap(arr, a, b):
    """
    exchange the data arr[a],arr[b],arr is the name of the list.

    :param arr: the name of list
    :param a: the index of being prepared exchange
    :param b: the index of being prepared exchange
    :return: the new list which has been exchanged.
    """
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t


arrs = [2, 7, 9, 10, 78, 23, 18, 17, 19]
simple_select_sort(arrs)
print(arrs)
