# Написать программу, которая подсчитывает количество символов в строке
# и формирует dict в котором key = буква, value= количество их в слове:
# Входная строка : 'Hillel school'
# Результат :{'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}

# преобразовываем строку в список
input_to_count: str = "Hillel school"
letters: list = list(input_to_count)
# создаем пустой словарь, чтобы в него писать.
dictionary: dict = {}

# для каждой буквы из списка считаем ее кол-во в списке и записываем
# в цикл
for i in letters:
    dictionary[i] = letters.count(i)
print(dictionary)



