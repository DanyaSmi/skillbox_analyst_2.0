# Задача 3. Кино
# Мы поддерживаем свой киносайт и хотим сделать так,
# чтобы пользователи после регистрации могли создать
# собственный рейтинг фильмов из тех, которые есть на сайте.
# Вот сам список фильмов (конечно же, можете брать свои):

films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

# Напишите программу, которая позволяет добавлять в свой
# рейтинг фильмы, удалять их оттуда, а также вставлять
# на нужное пользователю место. Обеспечьте контроль ввода
# и сделайте так, чтобы в список нельзя было добавить
# один и тот же фильм несколько раз.

# Пример:
# Ваш текущий топ фильмов: []
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить

# Ваш текущий топ фильмов: [‘Леон’]
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить
# Этот фильм уже есть в вашем списке.

# Ваш текущий топ фильмов: [‘Леон’]
# Название фильма: Матрица
# Команды: добавить, вставить, удалить
# Введите команду: добавить

# Ваш текущий топ фильмов: [‘Леон’, ‘Матрица’]
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: удалить

# Ваш текущий топ фильмов: [‘Матрица’]
# Название фильма: …..

my_list = []

def movie_exists(name, list):
    for i_name in list:
        if i_name == name:
            return True
    return False

while True:
    print(f'\nYour current list of favorite movies is: {my_list}')
    movie = input('Enter the name of movie: ')
    if movie_exists(movie, films):
        print('Commands: add, remove, insert.')
        command = input('Enter a command: ')
        if command == 'add':
            if movie_exists(movie, my_list):
                print('This movie exists in your list already.')
            else:
                my_list.append(movie)
        elif command == 'remove':
            if movie_exists(movie, my_list):
                my_list.remove(movie)
            else:
                print('There is not this movie in your list.')
        elif command == 'insert':
            if movie_exists(movie, my_list):
                print('This movie exists in your list already.')
            else:
                index = int(input('What number of position is it? '))
                my_list.insert(index - 1, movie)
    else:
        print('There is not this movie on the website.')
