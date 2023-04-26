# Задача 3. Собачьи бега
# В собачьих бегах участвует N собак, у каждой из них
# есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки.
# Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков
# поменялись местами! Нужно это исправить.

# Дан список очков из N собак.
# Напишите программу, которая меняет местами
# наибольший и наименьший элементы в списке.

points = []
N = int(input('Enter the number of dogs: '))
for _ in range(N):
    point = int(input('Enter the points for a dog: '))
    points.append(point)

max_index = 0
min_index = 0
for i in range(N):
    if points[i] > points[max_index]:
        max_index = i
    if points[i] < points[min_index]:
        min_index = i

points[max_index], points[min_index] = points[min_index], points[max_index]

print(f'List of points after swapping the largest and smallest elements: {points}')