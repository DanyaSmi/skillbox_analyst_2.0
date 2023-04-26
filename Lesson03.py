
print("Hello World")

#Задача 1. Таблица умножения: возвращение
#Математик Паша постепенно начал становиться программистом Пашей, правда  интернет ему не оплатили, а компьютер настолько древний, что просто не тянет никакие среды разработки. Поэтому он начал разбираться, как можно писать программы, используя только возможности операционной системы. 

#Напишите простую программу, которая выводит на экран таблицу умножения. Используйте только консоль и текстовый редактор.

s1 = int(input("Enter the biggest number: "))

for i in range(1, s1 + 1):
     for j in range(i, i * s1 + 1, i):
         print(j, end='\t')
     print()

#Задача 2. Калькулятор
#Напишите программу калькулятор. Пользователь вводит два числа A и B и действие X (плюс, минус, умножить, разделить). Программа выводит результат в виде A X B = C, где C — результат этого действия над числами A и B. Используйте только консоль и текстовый редактор. #Обеспечьте контроль ввода.

#Пример работы программы в консоли:
#Выберите операцию: +
#Введите первое число: 5
#Введите второе число: 6

#5 + 6 = 11


#Пример работы программы в консоли 2:
#Выберите операцию: №
#Ошибка: такой операции не существует. Попробуйте ещё раз.
#Выберите операцию: -
#Введите первое число: 5
#Введите второе число: 6

#5 - 6 = -1


# A function to check if numbers are entered correctly:

def input_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Enter a number. ")

# Enter the number A and B
a = input_number("Enter a number A: ")
b = input_number("Enter a number B: ")

# Enter an action:

while True:
    x = input("Enter an action (+, -, *, /): ")
    if x in ['+', '-', '*', '/']:
        break
    else:
        print("Error: Enter the correct action (+, -, *, /).")

# Result calculating and input on a screen:

if x == '+':
    c = a + b
elif x == '-':
    c = a - b
elif x == '*':
    c = a * b
else:
    c = a / b

print("{} {} {} = {}".format(a, x, b, c))

#Задача 3.

def input_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Ошибка: введите число.")

# Ввод действия X
while True:
    x = input("Введите действие (+, -, *, /): ")
    if x in ['+', '-', '*', '/']:
        break
    print("Ошибка: введите корректное действие (+, -, *, /).")

# Ввод количества операндов
while True:
    num_operands = int(input("Введите количество операндов: "))
    if num_operands >= 2:
        break
    print("Ошибка: количество операндов должно быть больше 1.")

# Ввод операндов
operands = []
for i in range(num_operands):
    operand = input_number("Введите операнд {}: ".format(i+1))
    operands += [operand]

# Вычисление результата и вывод на экран
if x == '+':
    c = sum(operands)
elif x == '-':
    c = operands[0] - sum(operands[1:])
elif x == '*':
    c = 1
    for operand in operands:
        c *= operand
else:
    c = operands[0] / (operands[1] * operands[2] * ... * operands[n-1])

operands_str = str(operands[0])
for i in range(1, num_operands):
    operands_str += "+"
    operands_str += str(operands[i])

print("{} = {}".format(operands_str, c))