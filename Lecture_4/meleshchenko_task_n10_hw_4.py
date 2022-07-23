# Блок с входными данными: пустым массивом
# и масссивом с вариантами пользовательских решений.
# я решил использовать массив, вместо простого принта с форматированием,
# так как, по моему мнению, такой код легче изменять и читать.

grid: list = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

user_decisions: list = ["1) Сделать запись",
                        "2) Получить значение по координатам",
                        "3) Показать все ячейки",
                        "4) Удалить значение по координатам",
                        "0) Программа завершает работу"]


# Весь блок отвечающий за вывод таблицы помещен в функцию,
# чтобы при необходимости вызова не приходилось копировать/вставлять
# большие куски кода
def grid_print():
    count_for_y: int = 4
    print("Y")
    for i in grid[-1::-1]:  # итерирование изменено, чтобы совпадали значения по осям.
        print("  +---+---+---+---+---+")
        print(count_for_y, *i, sep=" | ", end=" |\n")
        count_for_y -= 1
    print("  +---+---+---+---+---+", "X")
    print("    0   1   2   3   4   ")


# Это функция, отвечающая за вывод вариантов пользовательских решений
def user_decisions_print():
    for for_printing in user_decisions:
        print(for_printing)


# печатаем сетку
grid_print()
# объявляем переменную, чтобы цикл сразу мог с ней работать
user_decision: str = ""
# этим циклом мы обеспечиваем работу программы,
# пока пользователь не захочет с нее выйти
while user_decision != "0":
    user_decisions_print()
    user_decision: str = input("Пожалуйста, выбери действие: ")
    if user_decision == "1":
        print("Введите x и y в формате x=2;y=2;value='v'")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        value: str = input("value= ")
        if grid[x][y] == " ":
            grid[x][y] = value
            print("Запись сделана!")
        else:
            print("Эта ячейка занята! Перезаписать?\n1) Да\n2) Нет ")
            override_decision: str = input("Пожалуйста, сделай свой выбор: ")
            if override_decision == "1":
                grid[x][y] = value
            else:
                continue
    elif user_decision == "2":
        print("Введите x и y в формате x=2;y=2;")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        if grid[x][y] == " ":
            print("Пустая ячейка")
        else:
            print(grid[x][y])
    elif user_decision == "3":
        grid_print()
    elif user_decision == "4":
        print("Введите x и y в формате x=2;y=2;")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        grid[x][y] = " "
        print("Запись удалена!")

