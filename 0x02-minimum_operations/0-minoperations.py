#!/usr/bin/python3
'''A text editor can execute only two operations on a text file with a single
    character H, viz: `Copy All` and `Paste`. Given a number n, write a
    function that calculates the minimum number of operations needed to obtain
    exactly n H characters in the file.
'''


def prime_factors(n):
    '''Computes the prime factors of n

    Arg: n is a positive number whose prime factors are to be found

    Return: an array of prime factors of n
    '''
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            # factor out divisor from n since it's already included in factors
            n = n / divisor
        else:
            divisor = divisor + 1  # check the next number

    return factors


def minOperations(n):
    '''Computes the minimum number of `Copy All` and `Paste` operations needed
        to obtain exactly n number of a given character in a text file

    Arg: n is a positive integer (see function description above)

    Return: +ve int (see function desc), 0 if n chars are impossible to achieve
    '''
    min_num_op = 0
    count_factors = {i: prime_factors(n).count(i) for i in prime_factors(n)}

    for k, v in count_factors.items():
        # minimum number of operations to get n similar characters is the sum
        # of the product of each prime factor of n and its count
        min_num_op = min_num_op + (k * v)

    return min_num_op
