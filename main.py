def find_max(list):
# создаём переменную для хранения максимального числа в массиве
    max_number = list[0]
    for i in list:
       if i > max_number:
           max_number = i
    return max_number

numbers = [56, 74, 23, 98, 143, -89, -23]

def find_min(list):
    # создаём переменную для хранения минимального числа в массиве
    min_number = list[0]
    for i in list:
        if i < min_number:
            min_number = i
    return min_number

print(find_max(numbers))
print(find_min(numbers))