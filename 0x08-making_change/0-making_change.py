#!/usr/bin/python3
'''Make change'''


def makeChange(coins, total):
    if total < 1:
        return 0

    change = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total:
            change = change + 1
            total = total - coin

    if (total == 0):
        return change

    return -1
