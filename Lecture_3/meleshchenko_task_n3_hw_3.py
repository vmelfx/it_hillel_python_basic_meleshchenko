# Приветствует пользователя в произвольном виде.
# Принимает на ввод его никнейм, пол, возраст.
# Если никнейм содержит admin, выводит: "Привет, повелитель!"
# не прекращая работу.
# Если возраст больше 10 и меньше 14 и пол М или больше 30 и пол М:
# Выводит "Советую Вам посмотреть "StarWars" или 'Мандалорец'"
# Если возраст больше 22 и меньше 32 и пол Ж:
# Рекомендация "Советую Вам посмотреть "Трансформеры""
# Если возраст меньше 16 и пол Ж:
# Рекомендация "Советую Вам посмотреть "Инсургент""
# Если никнейм 'Женя': Рекомендация "Советую Вам посмотреть 'TENET'"
# Если возраст до 11 и пол М: Рекомендация "Советую Вам посмотреть "TMNT""
# Если никнейм Guido: Кроме рекомендации, выводит "Огромное спасибо!"


# Login page

print("Welcome to the club body!")
nickname: str = input("Please, enter your nickname: ")
gender: str = input("Please, enter your gender: ")

# checking if gender is filled correctly
if gender == "Male" or gender == "Female":
    age: str = input("Please, enter your age: ")
    if age.isdigit():  # # checking if age is filled correctly
        # noinspection PyTypeChecker
        age = int(age)
    else:
        print("Only numbers allowed in age")
        exit(1)
else:
    print("Please enter correct gender. Male or Female, without spaces")
    exit(1)
# Recommendations block

# Films to recommend
hello_lord: str = "Привет, повелитель!"
mandalorian: str = "Советую Вам посмотреть 'StarWars' или 'Мандалорец'"
transformers: str = "Советую Вам посмотреть 'Трансформеры'"
insurgent: str = "Советую Вам посмотреть 'Инсургент'"
tenet: str = "Советую Вам посмотреть 'TENET'"
tmnt: str = "Советую Вам посмотреть 'TMNT'"

# noinspection PyTypeChecker,PyUnboundLocalVariable
if nickname == "admin" or nickname == "Admin":
    print(hello_lord)
    input("Hit Enter to exit")
elif nickname == "Guido":
    print(tenet, end=" and ")
    print("Большое спасибо!")
elif nickname == "Женя":
    print(tenet)
elif 22 < age < 32 and gender == "Female":
    print(transformers)
elif 16 > age and gender == "Female":
    print(insurgent)
elif 11 > age and gender == "Male":
    print(tmnt)
elif 10 < age < 14 and gender == "Male" or age > 30 and gender == "Male":
    print(mandalorian)
