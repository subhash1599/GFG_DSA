def gcd_of_two_numbers_naive(number1, number2):
    res = min(number1, number2)

    while (res > 0):

        if number1 % res == 0 and number2 % res == 0:
            break
        res -= 1
    return res


print(gcd_of_two_numbers_naive(100, 200))


def gcd_of_two_numbers_efficient(number1, number2):

    while (number1 != number2):

        if number1 > number2:
            number1 = number1-number2
        elif number2 > number1:
            number2 = number2-number1
    return number1


print(gcd_of_two_numbers_efficient(100, 200))


def gcd_of_two_numbers_effcient_euclidean(number1, number2):
    if number2 == 0:
        return number1
    else:
        return gcd_of_two_numbers_effcient_euclidean(number2, number1 % number2)


print(gcd_of_two_numbers_effcient_euclidean(12, 15))
