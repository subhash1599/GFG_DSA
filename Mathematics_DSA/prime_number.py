from math import sqrt


def is_prime(number):

    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(is_prime(771))


def is_prime_optimized(number):

    if number == 1:
        return False
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            return False
    return True


print(is_prime_optimized(7))


def is_prime_effcient(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    if (number % 2 == 0 or number % 3 == 0):
        return False

    for i in range(5, int(sqrt(number)), 6):
        if number % i == 0 or number % (i+2) == 0:
            return False
    return True


print(is_prime_effcient(121))
