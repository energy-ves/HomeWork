numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_missing_number = 4
sum_of_numbers = sum(numbers[:index_missing_number]) + sum(numbers[index_missing_number + 1:])
count_of_numbers = len(numbers)
average = sum_of_numbers / count_of_numbers
numbers[index_missing_number] = average
print("Измененный список:", numbers)
