# Задача 1. Кубы и квадраты
# Пользователь вводит числа A и B.
# Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В,
# во втором — квадраты чисел в этом же диапазоне.
# Выведите списки на экран.
# Для генерации используйте list comprehensions (как и в следующих задачах).

# Пример:
# Левая граница: 5
# Правая граница: 10

# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

left = int(input('Enter the left boarder: '))
right = int(input('Enter the right boarder: '))
cubes = [x ** 3 for x in range(left, right + 1)]
squares = [x ** 2 for x in range(left, right + 1)]

print(f'The list of number cubs in the range from {left} to {right} is: {cubes}')
print(f'The list of number squares in the range from {left} to {right} is: {squares}')