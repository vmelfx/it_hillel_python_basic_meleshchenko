# Task: Написать 3 примера различных с оператором in
# написать 3 примера условия if elif else.

# Example 1
# It is simple example of cycles.
# It takes numbers from 1 to 100 and returns which is even number or not
for i in range(1, 101):
    if i % 2 == 0:
        print(i, "It is number number")
    else:
        print(i, "It it is not even number")

# Example 2
# In this example I ask user his name and return welcome message or not
# depending on input
allowed_names: str = "Vladimir"
input_name: str = input("Please enter your name: ")
welcome_message: str = "Welcome"
not_welcome_message: str = f"Get out of here, {input_name}"
if input_name in allowed_names:
    print(welcome_message)
else:
    print(not_welcome_message)

# Example 3
# Here I am taking a list with the name of US countries
# and returning its names with the number of letters.
countries: list = ["Washington Country", "Jefferson Country", "Franklin Country",
                   "Jackson Country", "Lincoln Country", "Madison Country",
                   "Clay Country", "Montgomery Country", "Union Country",
                   "Marion Country"]
for i in countries:  # in this case I need additional variable to exclude spaces from output
    a = str(i)
    a = a.replace(" ", "")
    print(i, '|', "Letters in name: ", len(a))
