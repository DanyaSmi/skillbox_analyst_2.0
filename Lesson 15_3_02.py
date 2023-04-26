# Задача 2. Соседи
# Дана строка S и номер позиции символа в строке.
# Напишите программу, которая выводит соседей этого символа
# и сообщение о количестве таких же символов среди этих соседей:
# их нет, есть ровно один или есть два таких же.

# Пример 1:
# Введите строку: abbc
# Номер символа: 3

# Символ слева: b
# Символ справа: c

# Есть ровно один такой же символ.

# Пример 2:
# Введите строку: abсd
# Номер символа: 3

# Символ слева: b
# Символ справа: d

# Таких же символов нет.

row = input('Enter the row: ')
sym_num = int(input('Enter a number of symbol: '))

#symbol_list = []
#if len(row) - 1 > sym_num > 1:
#	left_sym = row[sym_num - 1]
#	right_sym = row[sym_num + 1]
# else:
#	None

left_sym = row[sym_num - 1] if sym_num > 1 else None
right_sym = row[sym_num + 1] if sym_num < len(row) - 1 else None

same_sym = []
if left_sym == row[sym_num]:
    same_sym.append(left_sym)
if right_sym == row[sym_num]:
    same_sym.append(right_sym)

print(f'The let symbol: {left_sym}' if left_sym else 'There is not the let symbol.')
print(f'The right symbol: {right_sym}' if right_sym else 'There is not the right symbol')

if not same_sym:
    print('There are not equals symbols.')
elif len(same_sym) == 1:
    print('There is one the same symbol.')
else:
    print('There are two the same symbols.')


