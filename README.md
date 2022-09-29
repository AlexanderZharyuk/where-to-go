# WHERE TO GO
Website with interesting locations in Moscow.

- Website demo: [https://realvizy.pythonanywhere.com/](https://realvizy.pythonanywhere.com/)
- To login to the admin panel go to [https://realvizy.pythonanywhere.com/admin/](https://realvizy.pythonanywhere.com/admin/)


Preview:
![site preview]


## Features of the project
This project implemented:
1. Admin panel for easy adding of new places on the map
2. Map with places, their descriptions and pictures
3. Getting detailed data about the place via API
4. Custom command to load location via json file

## Setting up your development environment
To run the site on a local server, install the dependencies in the virtual environment with the command:
```shell
pip install -r requirements.txt
```

And also set environment variables in `.env` file:
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
STATIC_ROOT=<YOUR-STATIC-FOLDER-ABSOLUTE-PATH>
```

## Site launch
Run the migrations:
```shell
python3 manage.py migrate
```
Create your admin account:
```shell
python3 manage.py createsuperuser
```
Start the server:
```shell
python3 manage.py runserver
```
After that, your site will be launched at [http://127.0.0.1:8000/](http://127.0.0.1:8000/), the admin panel will be available at [http://127.0.0.1:8000/admin/ ](http://127.0.0.1:8000/admin/).

## Adding new places
You can add new places directly through the admin panel or with a custom command:
```shell
python3 manage.py load_place <url to json file with place data>
```
What should the json file look like?

The template for a file with data about some place is in the file `examples/place_example.json`

## Author
* [Alexander Zharyuk](https://github.com/AlexanderZharyuk)
