#Работает в обе стороны
def power(a, n):
    tmp = 1
    for i in range(abs(n)):
        tmp *= a
    if n >= 0:
        return tmp
    else:
        return 1 / tmp
    
print(power(5, -1))