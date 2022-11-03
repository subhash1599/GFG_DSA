def factorial(number):

    res = 1
    for i in range(2, number+1):
        res *= i

    return res


print(factorial(9))


def factorial_recursive(number):

    if number == 0:
        return 1
    return number*factorial(number-1)


print(factorial_recursive(5))
