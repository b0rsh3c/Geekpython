"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
#создаем список по одному из каждого типа данных
list_check = [1, 'eggs', ('1','2'), 46.9, [1,1,1], complex(5,6), {'key1' : 'word1'}, 
        True, b'text']
#1 способ проверки соответствия типов, оучше конечно функциб написать для такого

if isinstance(list_check[0], int):
  print("это INT")
else:
  print("Это не INT")
  
if isinstance(list_check[1], str):
  print("это строка")
else:
  print("Это не строка")
  
if isinstance(list_check[2], tuple):
  print("это кортеж")
else:
  print("Это не кортеж")

if isinstance(list_check[3], float):
  print("это FLOAT")
else:
  print("Это не FLOAT")

#2 способ проверки
if type(list_check[4]) is list:
  print("это список")
else:
  print("Это не список")
  
if type(list_check[5]) is complex:
  print("это комплексное число")
else:
  print("Это не список")
  
if type(list_check[6]) is dict:
  print("Это словарь")
else:
  print("Это не словарь")

if type(list_check[7]) is bool:
  print("это Логика")
else:
  print("Это не множество")
  
if type(list_check[8]) is bytes:
  print("Это байтовые строки")
else:
  print("Это не байтовые строки")