from itertools import count

for i in count(1):
    if i > 100:
        break
    else:
        print(i)