# Спросить у пользователя год рождения.
# Спомощью if -elif-else
# Проверить встроенным строковым методом состоит ли возраст
# из числа или текста
# если текст то по попросить ввести число.
# Если 21 год вывести “You should visit Holland.”
# Если больше 21 вывести “You should visit Vietnam.”
# Все остальные варианты. Вывести “Travell everywhere”


# тут я импортирую модуль datetime. Это выглядит странно,
# но я получаю класс datetime из модуля datetime.
# так как мне нужен только текущий год, то я буду импортировать только его.
from datetime import datetime
current_year = datetime.now().year
birth_date: str = input("Where were you born? ")
holland: str = "You should visit Holland"
vietnam: str = "You should visit Vietnam"

if birth_date.isdigit() is True:
    # noinspection PyTypeChecker
    birth_date = int(birth_date)
    # noinspection PyTypeChecker
    if current_year - birth_date == 21:
        print(holland)
    elif current_year - birth_date > 21:
        print(vietnam)
    else:
        print("Travel everywhere")
else:
    print("Please enter your birthday as number")
