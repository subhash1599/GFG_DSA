def isPlaindrome(number):

    temp = number
    rev = 0

    while (temp > 0):
        rev = rev*10+temp % 10
        temp = temp//10
    return rev == number


print(isPlaindrome(120))
