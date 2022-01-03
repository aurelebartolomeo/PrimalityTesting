import random


def mr(n, k):
    """
    Miller-Rabin algorithm for primality  testing

    Inputs:
     n: number to test for primality
     k: number of bases to choose

    Output:
     1 if probable prime, 0 otherwise
    """
    r, d = rd_decomposition(n)
    for i in range(k):
        a = random.randint(2, n - 2)
        x = (a ** d) % n
        if x == 1 or x == n - 1:
            continue
        break_indicator = False
        for j in range(r - 1):
            x = (x ** 2) % n
            if x == n - 1:
                break_indicator = True
                break
        if break_indicator:
            continue
        return 0
    return 1


def rd_decomposition(n):
    """
    return r and d such that n = 2^r * d +1
    """
    n = n - 1
    r = 0
    while n % 2 == 0:
        r += 1
        n = n // 2
    return r, n
