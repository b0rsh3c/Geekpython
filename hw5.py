from functools import reduce

list = [i for i in range(100,1001,2)]

#print(list)

result = reduce(lambda x,y: x * y, list)

print(result)