# Задание "Свой YouTube"
import time

class User:

    # Конструктор класса User
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash( password )
        self.age = age

    # Метод для сравнения никнеймов
    def __eq__(self, other):
        return self.nickname == other.nickname

    # Метод для вывода имени в виде строки
    def __str__(self):
        return self.nickname

    # Метод для хэша пароля
    def __hash__(self):
        return hash( self.password )


class Video:

    # Конструктор класса Video
    def __init__(self, title: str, duration: int, adult_mode=bool( False )):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    # Метод для сравнения названий видео
    def __eq__(self, other):
        return self.title == other.title

    # Метод для вывода названия видео в виде строки
    def __str__(self):
        return f'{self.title}'

    # Возвращение длины видео
    def dur(self):
        return self.duration

class UrTube:

    # Конструктор класса UrTube
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # Для регистрации нового пользователя
    def register(self, nickname: str, password: str, age: int):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.log_out()
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    # Для входа пользователя
    def log_in(self, nickname, password ):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return self.current_user

    # Для выхода пользователя
    def log_out(self):
        self.current_user = None

    # Для добавления нового видео в список Video
    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print(f'Видео с названием {i.title} уже существует')

    # Для вывода списка видео
    def get_videos(self, text):
        list_of_videos = []
        for i in self.videos:
            if text.lower() in i.title.lower():
                list_of_videos.append(str(i))
        return list_of_videos

    # Для просмотра видео (отсчета времени видео)
    def watch_video(self, video):
        if self.current_user and self.current_user.age < 18:
            print(f'Вам нет 18 лет. Пожалуйста, покиньте страницу')
        elif self.current_user:
            for i in self.videos:
                if video in i.title:
                    dur = Video.dur(i)
                    for j in range(1, dur + 1):
                        print(j, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

if __name__ == '__main__':

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