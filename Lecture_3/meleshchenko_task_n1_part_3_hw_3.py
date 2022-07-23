# Task: Написать 3 примера использования max(), min(),

# First example
a = 1, 2, 3, 4, 5, 6

print("The maximum of a tuple is: ", end="")
print(max(a))
print("The minimum of a tuple is: ", end="")
print(min(a))

# Second example
river_length: list = [6.650, 6.400, 6.300, 6.275, 5.539, 5.464, 5.410, 4.880, 4.700, 4.444]
print("The longest river on Earth is ", end="")
print(max(river_length), "km long")
print("The shortest river on Earth is: ", end="")
print(min(river_length), "km long")

# Third example
x: list = [10, 20, 30]
y: list = [5, 15, 40, 25]
print("The smallest object by length is: ", end="")
print(min(x, y, key=len))
print("The largest object by length is: ", end="")
print(max(x, y, key=len))
