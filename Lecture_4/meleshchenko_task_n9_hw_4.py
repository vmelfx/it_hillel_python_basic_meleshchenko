# Тема Листы
# Даны два списка элементов если хоть один елемент совпадает отпринтить True.
# print(Тrue) не слово! а объект подставить.

list_1: list = "Ready for action".split(" ")
list_2: list = "Not ready for action".split(" ")


for el in list_1:
    for el2 in list_2:
        if el == el2:
            print(el)
            exit(0)
