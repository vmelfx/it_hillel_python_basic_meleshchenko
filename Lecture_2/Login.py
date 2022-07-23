# Defining variables
user_name: str = input('What is your name? ')
user_age: int = int(input('How old are you? '))

# Messages for users on login
welcome_message = "Welcome {} on our website.".format(user_name)
too_young = "Dear {}, you need to wait one year.".format(user_name)
lucky_one = "You are lucky {} and welcome.".format(user_name)
not_real = "You are not real {}.".format(user_name)
far_to_young = "I'm sorry {} you are too young.".format(user_name)

if 70 <= user_age <= 90:
    print(lucky_one)
elif user_age > 121:
    print(not_real)
elif user_age == 16:
    print(too_young)
elif user_age > 16:
    print(welcome_message)
else:
    print(far_to_young)
