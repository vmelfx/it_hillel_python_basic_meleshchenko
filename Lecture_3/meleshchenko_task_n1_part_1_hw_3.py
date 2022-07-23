# Task: Создать файл (модуль) с примерами всех методов строк.
# all methods go in output order of dir(str)

a = "london"

# capitalize
# This method makes the first character have upper case and the rest lower
print(a.capitalize())

# casefold
# This method returns a version of the string suitable for caseless comparsion
print(a.casefold())

# center
# This method will center align the string, using a specified character
# (space is default) as the fill character.
print(a.center(12, "#"))

# count
# This method returns the number of times a specified value
# appears in the string.
print(a.count("n"))

# encode
# This method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
print(a.encode(encoding='ascii', errors='replace'))

# endswith
# This method returns True if the string ends with the specified value
# otherwise False.
print(a.endswith('.'))

# expandtabs
# This method sets the tab size to the specified number of whitespaces.
b = '0\t1\t22\t333\t4444\t55555\t666666'
print(b.expandtabs())

# find
# This method finds the first occurrence of the specified value.
# Method returns -1 if the value is not found.
print(a.find('n'))

# format
# This method method formats the specified value(s)
# and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# Returns formated string.
b = "My name is {0}, I'm {1} years old".format("Vladimir", 22)
print(b)

# index
# This method finds the first occurrence of the specified value.
# method raises an exception if the value is not found.
# method is almost the same as the find() method
# the only difference
# is that the find() method returns -1 if the value is not found.
print(a.index("n"))

# isalnum
# method returns True if all the characters are alphanumeric
# meaning alphabet letter (a-z) and numbers (0-9)
print(a.isalnum())

# isalpha
# method returns True if all the characters are alphabet letters (a-z)
print(a.isalpha())

# isascii
# method returns True if all the characters are ascii characters  (a-z).
print(a.isascii())

# isdecimal
# method returns True if all the characters are decimals (0-9)
print(a.isdecimal())

# isdigit
# method returns True if all the characters are digits, otherwise False
print(a.isdigit())

# isidentifier
# method returns True if the string is a valid identifier, otherwise False
# A string is considered a valid identifier if it only contains
# alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces
print(a.isidentifier())

# islower
# method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
print(a.islower())

# isnumeric
# method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
print(a.isnumeric())

# isprintable
# method returns True if all the characters are printable, otherwise False.
print(a.isprintable())

# isspace
# method returns True if all the characters in a string are whitespaces
# otherwise False.
print(a.isspace())

# istitle
# method returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False.
print(a.istitle())

# isupper
# method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
print(a.isupper())

# join
# method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator
print(a.join(b))

# ljust
# method will left align the string,
# using a specified character (space is default) as the fill character.
print(a.ljust(10, "."))

# lower
# method returns a string where all characters are lower case.
# Symbols and Numbers are ignored
print(a.lower())

# lstrip
# method removes any leading characters
# (space is the default leading character to remove)
print(a.lstrip("l"))

# maketrans
# method returns a mapping table that can be used
# with the translate() method to replace specified characters.
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

# partition
# method searches for a specified string, and splits the string
# into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.

txt = "I'm a python developer"
print(txt.partition("python"))

# removeprefix
# removes the prefix and returns the rest of the string.
# If the prefix string is not found then it returns the original string.
print(txt.removeprefix("I'm"))

# removesuffix
# removes the suffix and returns the rest of the string.
# If the suffix string is not found then it returns the original string.
print(txt.removesuffix("developer"))

# replace
# method replaces a specified phrase with another specified phrase
print(txt.replace("python", "java"))

# rfind
# method finds the last occurrence of the specified value.
# method returns -1 if the value is not found.
print(txt.rfind("e"))

# rjust
# method finds the last occurrence of the specified value.
# method raises an exception if the value is not found.
print(txt.rindex("r"))

# rpartition
# method searches for the last occurrence of a specified string
# and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.#
# The third element contains the part after the string.
print(txt.rpartition("a"))

# rsplit
# method splits a string into a list, starting from the right.
# If no "max" is specified
# this method will return the same as the split() method.
# When maxsplit is specified
# the list will contain the specified number of elements plus one.
print(txt.rsplit(", ", 1))

# rstrip
# method removes any trailing characters (characters at the end a string)
# space is the default trailing character to remove
txt = "I'm a python developer            "
print(txt.rstrip())

# split
# method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# When maxsplit is specified
# the list will contain the specified number of elements plus one.
print(txt.split("'"))

# splitlines
# method splits a string into a list.
# The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())

# startswith
# method returns True if the string starts with the specified value
# otherwise False.
print(txt.startswith("Thank"))

# strip
# method removes any leading (spaces at the beginning)
# and trailing (spaces at the end) characters
# space is the default leading character to remove
print(txt.strip())

# swapcase
# method returns a string where all
# the upper case letters are lower case and vice versa.
print(txt.swapcase())

# title
# method returns a string where the first character in every word is upper case
# Like a header, or a title.
# If the word contains a number or a symbol
# the first letter after that will be converted to upper case.
print(txt.title())

# translate method i used before in an example of maketrans

# upper
# method returns a string where all characters are in upper case.
print(txt.upper())

# zfill
# method adds zeros (0) at the beginning of the string
# until it reaches the specified length.
print(txt.zfill(50))
