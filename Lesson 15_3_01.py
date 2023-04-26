# Задача 1. Текстовый редактор: возвращение
# Мы продолжаем участвовать в разработке нового текстового редактора
# и делать жизнь обычных пользователей чуть лучше.
# В этот раз у нас стоит задача сделать фишку с поиском и заменой символов
# в выделенной строчке. Например, человек что-то перечислял в тексте,
# но ошибся и вместо точек с запятой использовал двоеточия. Лингвисты негодуют.

# Пользователь вводит строку S.
# Напишите программу, которая заменяет в строке
# все двоеточия (:) на точки с запятой (;).
# Также подсчитайте количество замен и выведите ответ на экран
# (и новую строку тоже). Для решения используйте список.

# Пример:
# Введите строку: гвозди:шурупы:гайки

# Исправленная строка: гвозди;шурупы;гайки
# Кол-во замен: 2

s = input('Enter a string: ')  # prompt the user to enter a string

count = 0  # initialize a variable to keep track of the number of replacements
new_s = ''  # initialize a new string variable to store the modified string

# loop through each character in the string
for char in s:
    if char == ":":
        new_s += ";"  # replace ":" with ";"
        count += 1  # increment the count of replacements
    else:
        new_s += char  # add the character to the new string

# output the modified string and the count of replacements
print("Modified string:", new_s)
print("Number of replacements:", count)