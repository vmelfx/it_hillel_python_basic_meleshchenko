# Программа принимает список продуктов
# и принтит самое длинное слово и его длинну.
# Ипользовать ''.format() для вывода строки и аргументов.
# Входные данные: ['bread', 'milk', 'kolbasa']
# Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'

grocery_list: list = ['bread', 'milk', 'kolbasa']
# noinspection PyTypeChecker
max_len: str = max(grocery_list, key=len)
len_for_output: int = len(max_len)
output: str = "Самое длинное название продукта {} длина {}".format(max_len, len_for_output)
print(output)
