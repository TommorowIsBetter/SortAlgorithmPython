#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/2/18 16:27
"""


def quick_sort(numbers, left, right):
    """
    a demo quick sort algorithm with python language.

    :param numbers:
    :param left:
    :param right:
    :return:
    """
    if right - left <= 0:
        return numbers
    tmp = numbers[left]
    i = left + 1
    j = right

    while i < j:
        while numbers[j] > tmp and i < j:
            j -= 1
        while numbers[i] <= tmp and i < j:
            i += 1
        numbers[i], numbers[j] = numbers[j], numbers[i]
    if numbers[i] > numbers[left]:
        numbers[i -1], numbers[left] = numbers[left], numbers[i -1]
    else:
        numbers[i], numbers[left] = numbers[left], numbers[i]

    quick_sort(numbers, left, i - 1)
    quick_sort(numbers, i + 1, right)
    return numbers


test = [6, 7, 8, 5, 1, 2, 11, 5, 4]
print(quick_sort(test, 0, len(test) - 1))
