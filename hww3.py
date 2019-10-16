def my_func(var1, var2, var3):
    if (var1 > var2) & (var2 > var3):
        print(var1, var2)
    elif (var1 < var2) & (var2 < var3):
        print(var2, var3)
    elif (var1 > var2) & (var2 < var3):
        print(var1, var3)
    elif (var1 < var2) & (var2 > var3):
        if var1 > var3:
            print(var2, var1)
        else:
            print(var2, var3)
    