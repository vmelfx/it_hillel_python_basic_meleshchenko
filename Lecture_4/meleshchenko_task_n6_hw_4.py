# Тема Кортеж и работа сним.
# Удалить элемент из кортежа.
# Входные данные: (1, 2, 3)
# Результат: (1, 2)

input_tuple: tuple = (1, 2, 3)
# tuple is an immutable data type
# it is impossible to remove element from the tuple
# we can only re-declare tuple without selected element
input_tuple: tuple = (1, 2)
print(input_tuple)