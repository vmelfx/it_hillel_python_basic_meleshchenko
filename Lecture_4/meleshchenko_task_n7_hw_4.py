# Написать программу которая данный список кортежей переведет в список списков
# Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

input_data: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
processed_data: list = []

for tuples in input_data:
    converted_tuples: list = list(tuples)
    processed_data.append(converted_tuples)
print(processed_data)
