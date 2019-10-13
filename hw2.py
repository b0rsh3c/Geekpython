elem = [int(i) for i in input("Введи числа через пробел: ").split()]
for i in range(0, len(elem) - 1, 2):
    elem[i], elem[i+1] = elem[i+1], elem[i]
print(elem)