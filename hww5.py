def fun(lst):
    lst = lst.split()
    next = []
    for i in lst:
        next.append(int(i))
    return sum(next)
 
s = 0
while 1:
    lst = input("Введи число: ")
    if (lst == 'quit') | (lst == 'exit') : break
    s += fun(lst)
    print('Summa:', s)