def trialing_zeros_factorial(number):

    fact = 1
    for i in range(2, number+1):
        fact *= i
    res = 0
    while (fact % 10 == 0):
        res += 1
        fact = fact//10
    return res


print(trialing_zeros_factorial(10))


def trailing_zeros_factorial_efficient(number):

    if number < 0:
        return -1
    count = 0
    while (number >= 5):
        number = number//5
        count = count+number
    return count


# counting number of 5's in prime factors of the number
# The trailing zeros equal to number of 5's in the number while writing as prime factors
print(trailing_zeros_factorial_efficient(251))


# print(trailing_zeros_factorial_efficient(251))
