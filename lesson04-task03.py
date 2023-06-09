# Задача 3. Сессия
# Для сдачи зачёта студент Пётр написал программу, которая по координатам двух точек определяет уравнение прямой,
# проходящей через эти две точки, в виде y = k * x + b, где k и b — числа, означающие угловой коэффициент и
# вертикальное смещение прямой.Вот текст этой программы:

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

if x1 == x2:
    print("Уравнение прямой: x =", x1)
elif y1 == y2:
    print("Уравнение прямой: y =", y1)
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print("Уравнение прямой: y = " + str(k) + " * x + " + str(b))

# Пример работы программы(содержимое консоли):
# Введите первую точку
# X: 10
# Y: 20

# Введите вторую точку
# X: 15
# Y: 25
# Уравнение прямой, проходящей через эти точки:
# y = 1.0 * x + 10.0

# Однако вечером накануне сдачи Пётр обнаружил, что программа не всегда работает правильно.
# Например, она не выдаёт корректное уравнение, если координаты первой точки равны(10, 20),
# а координаты второй точки равны(10, 45).Отчаявшись и предвидя бессонную ночь, Пётр обратился к
# вам за помощью.Помогите ему найти и исправить ошибку в коде с помощью брейк - поинтов, чтобы уравнение прямой
# составлялось правильно во всех случаях.Используйте PyCharm.
