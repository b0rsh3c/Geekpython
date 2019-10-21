#генерация нужна была через рандом?
list = []
for j in range(1, 20):
    list.append(j)
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        print(list[i])
