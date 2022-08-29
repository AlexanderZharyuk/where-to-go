# WHERE TO GO
Сайт с интересными локациями в Москве.

- Демка сайта: [https://realvizy.pythonanywhere.com/](https://realvizy.pythonanywhere.com/)
- Для входа в админку перейдите по адресу [https://realvizy.pythonanywhere.com/admin/](https://realvizy.pythonanywhere.com/admin/)


Превью:
![site preview](https://user-images.githubusercontent.com/103115934/186663184-dcbcb7c5-0818-4618-9ca6-1c735a2b78b6.png)


## Фишки проекта
В данном проекте реализованы:
1. Админка, для удобного добавления новых мест на карте
2. Карта с местами, их описаниями и картинками
3. Получение подробных данных о месте по API
4. Кастомная команда для загрузки места через json-файл

## Предустановка
Для запуска сайта на локальном сервере, установите зависимости в виртуальное окружение командой:
```shell
pip install -r requirements.txt
```

А также настройте переменные окружения в `.env`-файле:
```
DJANGO_SECRET_KEY=<YOUR-DJANGO-SECRET-KEY>
DEBUG=True
ALLOWED_HOSTS=*
CSRF_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=False
SECURE_HSTS_PRELOAD=False
SECURE_SSL_REDIRECT=False
```

## Запуск сайта
Выполните миграции: 
```shell
python3 manage.py migrate
```
Создайте свой аккаунт в админке:
```shell
python3 manage.py createsuperuser
```
Запустите сервер:
```shell
python3 manage.py runserver
```
После чего ваш сайт запуститься по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/), админка будет доступна по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Добавление новых мест
Вы можете добавлять новые места напрямую через админку или при помощи кастомной команды:
```shell
python3 manage.py load_place <url на json-файл с данными о месте>
```
Как должен выглядеть json-файл?

Шаблон файла с данными о каком-то месте лежит в файле `examples/place_example.json`

## Автор
* [Alexander Zharyuk](https://github.com/AlexanderZharyuk)