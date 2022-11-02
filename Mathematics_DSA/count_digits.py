def countDigits(number):
    count = 0
    while (number > 0):
        number = number//10
        count = count+1
    return count


print(countDigits(12234567))
