# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В
# (можно сгенерировать случайно, при этом А < B).
# Напишите программу, которая удаляет элементы списка
# с индексами от А до В. Не используйте дополнительные
# переменные и методы списков.

import random

a = random.randint(1, 9)
b = random.randint(a + 1, 10) # изменение условия
n = random.randint(1, 10)

list_01 = []
for _ in range(n):
    list_01.append(random.randint(1, 1000))

list_02 = list_01[:]
list_03 = list_01[:]

del list_02[a:b+1] # удаление элементов из list_02
# list_fin = list_03[:a] + list_03[b:]

print("a =", a)
print("b =", b)
print("n =", n)
print("list_01 =", list_01)
print("list_fin =", list_02)