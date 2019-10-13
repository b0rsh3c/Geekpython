words = input("Введи слова через пробел: ").split()
#words.split()  - я объединил две строки в одну
# можно сократить решение до двух строк
"""
for word in input("Введи слова через пробел: ").split():
    print(word)

"""
print()
print("Cлова в столбец: ")
for word in words:
    print(word)