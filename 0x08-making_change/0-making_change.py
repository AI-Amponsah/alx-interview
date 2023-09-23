#!/usr/bin/python3
"""This module defines a function `makeChange`"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a
        given amount total
    """
    coins.sort(reverse=True)
    coin_count = 0
    remainder = 0

    if total <= 0:
        return 0
    for coin in coins:
        if total == 0:
            break
        elif coin <= total:
            remainder = total % coin
            coin_count += int(total / coin)
            total = remainder

    return coin_count if total == 0 else -1
