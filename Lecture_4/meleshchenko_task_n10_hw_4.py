pidary_1: list = "Марины a пидарасы".split(" ")
pidary_2: list = "Бумеранги a пидарасы".split(" ")


for el in pidary_1:
    for el2 in pidary_2:
        if el == el2:
            print(True)
            exit(0)

print(id(el))
print(id(el2))
