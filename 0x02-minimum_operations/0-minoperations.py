#!/usr/bin/python3
""" minimum operation using only copy all and paste """


def minOperations(n):
    """method calculate the minimum possible number of operations needed
       to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
