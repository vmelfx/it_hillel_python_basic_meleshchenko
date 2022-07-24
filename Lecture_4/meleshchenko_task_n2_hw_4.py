# Написать программу, которая подсчитывает количество символов в строке
# и формирует dict в котором key = буква, value= количество их в слове:
# Входная строка : 'Hillel school'
# Результат :{'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}

# convert string to list
input_to_count: str = "Hillel school"
letters: list = list(input_to_count)
# create an empty dictionary to write to
dictionary: dict = {}

# for each letter from the list, count its number in the list and print
for i in letters:
    dictionary[i] = letters.count(i)
print(dictionary)



