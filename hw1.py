import sys

arguments = sys.argv[1:]
rate = int(arguments[0])
production = int(arguments[1])
prize = int(arguments[2])
result = rate * production + prize
print("Зарплата равна ", result)

        