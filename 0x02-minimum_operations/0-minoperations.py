#!/usr/bin/python3

"""Minimum Operations"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations"""
    min_operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            min_operations += divisor
            n //= divisor
        divisor += 1

    return min_operations
