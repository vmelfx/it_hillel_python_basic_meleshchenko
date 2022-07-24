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


# The entire block responsible for displaying the table
# is placed in a function
# so you don't have to copy/paste big chunks of code if you need to call it

def grid_print():
    count_for_y: int = 4
    print("Y")
    for i in grid[-1::-1]:  # iteration changed to match axis values
        print("  +---+---+---+---+---+")
        print(count_for_y, *i, sep=" | ", end=" |\n")
        count_for_y -= 1
    print("  +---+---+---+---+---+", "X")
    print("    0   1   2   3   4   ")


# This is the function responsible for displaying user's decisions
def user_decisions_print():
    for for_printing in user_decisions:
        print(for_printing)


# print grid
grid_print()
# declare a variable so that, the loop can immediately work with it
user_decision: str = ""
# with this cycle we ensure the operation of the program, until the user wants
# to log out
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
                print("Запись сделана!")
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
        if grid[x][y] == " ":
            print("Эта ячейка уже пустая!")
        else:
            grid[x][y] = " "
            print("Запись удалена!")
    else:
        print("Please, choose one of decisions below:")
