# Task: Создать по 3 варинта всех уже изученных объектов в Пайтоне.
# строки.
# числа(с плавающей точкой, целочисленные)
# Списки
# Словари
# Кортежи

# strings
print("Strings:")
x: str = "London is a capital of Great Britain"
y: str = "I'm a python developer"
z: str = "My phone number is: 911"
print(x, y, z, sep='\n')
print()

# numbers
print("Numbers:")
x: int = 10
y: float = 36.6
z: float = 3.14
print(x, y, z, sep='\n')
print()

# lists
print("Lists:")
x: list = [1, 2, 3, 4, 5]
y: list = list("London is a capital of Great Britain".replace(' ', ''))
z: list = [1, 'hello', True, 1.25]
print(x, y, z, sep='\n')
print()

# dictionaries
print("Dictionaries:")
x: dict = {'персона': 'человек',
           'марафон': 'гонка бегунов длиной около 26 миль',
           'противостоять': 'оставаться сильным, несмотря на давление',
           'бежать': 'двигаться со скоростью'}

y: dict = {'car': 'porsche',
           'plane': 'cesna',
           'metal': 'Sabaton',
           'videcard': 'Nvidia'}

z: dict = {'brand': "Ford",
           'model': "Mustang",
           'year': 1964}

print(x, y, z, sep='\n')
print()
# QUESTION: Как должны форматироваться словари по пепу? Так как сделал я ок?

# tuples
print("Tuples:")
x: tuple = (3, 4)
y: tuple = (3, 3, 'x', [1,2])
z: tuple = 3, 4, 5, 6
print(x, y, z, sep='\n')
