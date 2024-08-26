def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(7))