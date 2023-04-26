# Задача 2. Кратность
# Пользователь вводит список из N чисел и число K.
# Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.

# Пример:
# Кол-во чисел в списке: 4
# Введите 1 число: 1
# Введите 2 число: 20
# Введите 3 число: 30
# Введите 4 число: 4

# Введите делитель: 10

# Индекс числа 20: 1
# Индекс числа 30: 2
# Сумма индексов: 3

nums_list = []
N = int(input('Enter the quantity of numbers in the list: '))
for i in range(N):
    num = int(input('Enter a number: '))
    nums_list.append(num)

K = int(input('Enter a divisor K: '))

sum_index = 0
i = 0
while i < N:
    if nums_list[i] % K == 0:
        sum_index += i
        print(f'The index of the number {nums_list[i]} is {i}')
    i += 1

print(f'Sum of indexes of elements in the list that are multiples of K: {sum_index}')
