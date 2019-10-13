print("Введите издержки")
iz = int(input())
print("Введите выручку")
vr = int(input())
if vr > iz:
    print("прибыль")
    pr = (vr - iz) / vr * 100
    print("рентабельность выручки", pr, "%")
else:
    print(" убыток")
print("численность сотрудников фирмы")
sotr = int(input())
result = pr / sotr
print("прибыль фирмы в расчете на одного сотрудника = ", result)

