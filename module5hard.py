import time  # Для паузы между секундами


class UrTube:
    '''
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    '''
    users = []
    videos = []
    current_user = None

    def __init__(self):
        return

    def __str__(self):
        return f'Количество пользователей: {len(self.users)}\n Количество видео: {len(self.videos)}'

    def log_in(self, nickname, password):
        # Хешируем введённый пароль для сравнения с сохранённым
        hashed_password = hash(str(password))
        # Ищем пользователя с таким же ником и хешем пароля
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                UrTube.current_user = user  # Меняем текущего пользователя на найденного
                print(f'Пользователь {nickname} успешно вошёл в систему.')
                return True
        print('Неверный логин или пароль.')
        return False

    def register(self, nickname, password, age):
        # Проверяем, существует ли уже пользователь с таким nickname
        for user in self.users:
            if user.nickname == nickname:
                print(f'\nПользователь {nickname} уже существует')
                return False
        # Если пользователь не найден, создаем нового
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Выполняем автоматический вход
        print(f'\nПользователь {nickname} успешно зарегистрирован и вошел в систему.')
        return True

    def log_out(self):
        self.current_user = None
        print(f'\nПользователь "обнулен"')
        return self.current_user

    def add(self, *args):
        """
        Принимает несколько видео (через *args) и добавлять их в список videos,
        если видео с таким названием ещё не существует.
        :param args:
        :return:
        """
        for video in args:
            # Проверка, что объект является экземпляром класса Video
            if isinstance(video, Video):
                # Проверяем, есть ли видео с таким же названием
                if not any(existing_video.title == video.title for existing_video in self.videos):
                    self.videos.append(video)
                    print(f'Видео "{video.title}" добавлено.')
                else:
                    print(f'Видео "{video.title}" уже существует.')
            else:
                # Выводим сообщение, если объект не является видео
                print(f'Объект {video} не является видео и не был добавлен.')

    def get_videos(self, search_word):
        """
        :param search_word: поисковое слово
        :return: found_videos: возвращать список названий всех видео, содержащих это слово (регистр игнорируется)
        """
        search_word_lower = search_word.lower()
        found_videos = [video.title for video in self.videos if search_word_lower in video.title.lower()]  # Супер
        # емко создаем список по списку найденых видео по списку видео

        if found_videos:
            print(f'Найдено видео по запросу "{search_word}": {", ".join(found_videos)}')
        else:
            print(f'Видео по запросу "{search_word}" не найдено.')
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Находим видео по точному совпадению названия
        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print(f'Видео "{title}" не найдено.')
            return

        # Проверка на возрастное ограничение
        if video.adult_mode and self.current_user.age < 18:
            print(f'Вам нет 18 лет, пожалуйста покиньте страницу.')
            return

        print(f'Начинаем просмотр видео: {video.title}')
        # Воспроизводим видео, секунду за секундой
        for second in range(video.time_now, video.duration):
            print(f'Просмотр: {second + 1}-я секунда')
            time.sleep(1)  # Пауза в 1 секунду между выводом

        video.time_now = 0  # Сбрасываем текущее время просмотра
        print(f'Конец видео "{video.title}".')


class Video:
    """
    Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
    (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now=0, adult_mode=18, bool=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.bool = bool
        # UrTube.videos.append(self)  # опционально автоматически добавляем текущий объект в список videos класса UrTube


class User:
    ''' Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число) '''

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = self.hash_password(password)  # Сохраняем хэш пароля
        self.age = int(age)
        UrTube.users.append(self)  # Добавляем текущий объект в список users класса UrTube

    def hash_password(self, password):
        """
        Хэширование пароля
        """
        password = str(password)
        hash_password = hash(password)
        return hash_password

    def __str__(self):
        return f'Пользователь: {self.nickname},\nDозраст: {self.age},\nХэш пароля: {self.password}'


# us_petka = User('Petka', 1234, 23)
# print(f'\n{us_petka}')
# us_vovka = User('Vovka', 111, 16)
# print(f'\n{us_vovka}')
#
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# print(f'\n{ur}')
# v0 = Video('Программист на работе', 120)
# v4 = Video('Васян. на работе', 120)
# ur.add(v0, v4, v99:=99)

# ur.log_in('Vasyan', 1212)
# ur.log_in('Vovka', 111)
# ur.register('Niky', 1010, 13)
# print(f'\nВ системе: \n {ur.current_user}')
# ur.register('Petka', 'newpassword', 25)
# ur.log_out()
# print(f'\nВ системе: \n {ur.current_user}')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')