txt: str = 'черт его возьми, черт его знает, Чертополох, иди к черту, черт ногу сломит, Чертеж здания в разрезе'
words = txt.split(' ')

print(words)
removal_template: str = 'черт'
processed_words: list = []
for word in words:
    if removal_template == word:
        processed_words.append("####")
    else:
        processed_words.append(word)
new_txt: str = " ".join(processed_words)
print(new_txt)
