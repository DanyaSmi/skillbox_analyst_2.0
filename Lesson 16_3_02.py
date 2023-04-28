# Задача 2. Вредоносное ПО
# Гера решил попрактиковаться в программировании
# и захотел написать небольшой скрипт, который
# после двух сообщений отправляет ещё одно на основе первых двух.

# Пользователь вводит две строки. В каждой из них есть какое-то
# количество специальных символов ! и ?. Напишите программу,
# которая считает количество этих символов отдельно в первой
# строке и отдельно во второй. Если в первой строке их больше,
# чем во второй, то на экран выводится первая строчка,
# объединённая со второй, а иначе — вторая с первой. При равном
# количестве символов в строках выводится «Ой».

# Пример 1:
# Первое сообщение: Привет!
# Второе сообщение: Как дела? Что делаешь?

# Третье сообщение: Как дела? Что делаешь? Привет!

# Пример 2:
# Первое сообщение: Хм!!
# Второе сообщение: ?

# Третье сообщение: Хм!!?

# third_mes = []

# while True:
# 	first_mes = input('Enter the first message: ')
#	ques_1 = first_mes.count('?')
#	excl_1 = first_mes.count('!')
#	sum_1 = ques_1 + excl_1
#	second_mes = input('Enter the second message: ')
#	ques_2 = second_mes.count('?')
#	excl_2 = second_mes.count('!')
#	sum_2 = ques_2 + excl_2
#	if sum_1 > sum_2:
#		third_mes.append(first_mes)
#		third_mes.append(second_mes)
#		print(f'The third message is: {third_mes}')
#	elif sum_1 < sum_2:
#		third_mes.append(second_mes)
#		third_mes.append(first_mes)
#		print(f'The third message is: {third_mes}')
#	else:
#		third_mes.append('Ohh')
#		print(f'The third message is: {third_mes}')
#	third_mes = []

while True:
# запрашиваем две строки у пользователя
	message1 = input('The first message: ')
	message2 = input('The second message: ')

# подсчитываем количество специальных символов в каждой строке
	count1 = message1.count('!') + message1.count('?')
	count2 = message2.count('!') + message2.count('?')

# объединяем строки в соответствии с условием
	if count1 > count2:
		result = message1 + ' ' + message2
	elif count2 > count1:
		result = message2 + ' ' + message1
	else:
		result = 'Ой'

# выводим результат
	print('The third message: ', result)