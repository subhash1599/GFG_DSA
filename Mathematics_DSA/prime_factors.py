from math import sqrt


def is_prime(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(sqrt(number)), 6):
        if (number % i == 0) or (number % (i+2) == 0):
            return False
    return True


def prime_factors(number):
    for i in range(2, number):
        if is_prime(i):
            x = i
            while (number % x == 0):
                print(i)
                x = x*i


prime_factors(315)


def prime_factors_efficient(number):
    if number <= 1:
        return
    for i in range(2, int(sqrt(number))):
        while (number % i == 0):
            print(i)
            number = number//i
    if number > 1:
        print(number)


prime_factors_efficient(84)


print("MOST EFFICIENT")


def prime_factors_most_effcient(number):

    if (number <= 1):
        return

    while (number % 2 == 0):
        print(2)
        number = number//2

    while (number % 3 == 0):
        print(3)
        number = number//3

    for i in range(5, int(sqrt(number)), 6):
        while (number % i == 0):
            print(i)
            number = number//i

        while (number % (i+2) == 0):
            print(i+2)
            number = number//(i+2)

    if number > 3:
        print(number)


prime_factors_most_effcient(25)
