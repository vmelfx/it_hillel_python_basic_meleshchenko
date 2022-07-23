# Task:
# написать программку которая будет состоять из первых двух и
# последних двух символов предоставленной строки.
# Если длинна строки меньше двух символов напечатать строку типа.
# 'Ваша строка слишком короткая - СТРОКА ' .
# Через метод форматирования строк с %.
# Входная строка : 'Hillel school'
# Результат1 : 'Hiol'
# или
# Результат2 : 'Ваша строка слишком короткая - и ваша строка'

input_string: str = input("Please enter your string: ")
if len(input_string) < 2:
    output_string: str = "Ваша строка слишком короткая - %s" % input_string
    print(output_string)
else:
    first_cut: str = input_string[:2]
    second_cut: str = input_string[-2:]
    output_string: str = first_cut + second_cut
    print(output_string)
