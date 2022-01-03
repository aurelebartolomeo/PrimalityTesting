import random


def fermat(n, k):
    """
    fermat algorithm for primality testing

    Inputs:
     n: number to test for primality
     k: number of bases to choose

    Output:
     1 if probable prime, 0 otherwise
    """
    for i in range(k):
        a = random.randint(2, n-2)
        if (a ** (n-1)) % n != 1:
            return 0
    return 1
