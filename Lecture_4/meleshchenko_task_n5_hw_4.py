# Пользователь вводит через запятую последовательность слов
# например цвета или продукты.
# Программа возвращает уникальные слова отсортированные по алфавиту.
# Входные данные: red, white, black, red, green, black
# Результат: black, green, red, white

# цикл проходит по всем элементам и отбирает уникальные в другой список.
# после этого стандартным методом их сортируем и выводим.

input_data: list = ["red", "white", "black", "red", "green", "black"]
processed_data: list = []
for elements in input_data:
    if elements not in processed_data:
        processed_data.append(elements)
processed_data.sort()
print(processed_data)
