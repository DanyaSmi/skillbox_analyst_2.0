# Задача 1. Список чётных чисел
# Пользователь вводит два числа: А и В.
# Реализуйте код, который генерирует список
# из чётных чисел в диапазоне от А до B.
# Используйте list comprehensions (как и в следующих задачах).

left = int(input('Enter the left boarder: '))
right = int(input('Enter the right boarder: '))

even_list = [x for x in range(left, right + 1) if x % 2 == 0]
print(even_list)