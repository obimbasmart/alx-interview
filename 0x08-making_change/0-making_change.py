#!/usr/bin/python3

"""Makding Change"""

from typing import List


def makeChange(coins: List, total: int) -> int:
    """return fewest number of coins needed to meet total"""
    n_coins = 0
    sorted_coins = sorted(coins, reverse=True)
    if total <= 0:
        return n_coins

    for coin in sorted_coins:
        n_coins += total // coin
        total = total % coin

    if total > 0:
        return -1
    return n_coins
