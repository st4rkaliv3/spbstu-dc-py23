numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# заменить значение пропущенного элемента средним арифметическим
i_none = 4
avg = sum(numbers[:i_none] + numbers[i_none + 1:]) / len(numbers)
numbers_new = numbers[:i_none] + [avg] + numbers[i_none + 1:]

print("Измененный список:", numbers_new)
