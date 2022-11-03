def lcm_of_two_numbers(number1, number2):
    res = max(number1, number2)

    while (True):
        if res % number1 == 0 and res % number2 == 0:
            return res
        res += 1


print(lcm_of_two_numbers(4, 6))


def gcd_of_two_numbers_efficient(number1, number2):

    if number2 == 0:
        return number1
    else:
        return gcd_of_two_numbers_efficient(number2, number1 % number2)


def lcm_effcient(number1, number2):
    return (number1*number2)//gcd_of_two_numbers_efficient(number1, number2)


gcd_of_two_numbers_efficient(4, 6)
print(lcm_effcient(4, 6))
