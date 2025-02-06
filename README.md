## Проект Foodgram - сайт с рецептами.


### Возможности проекта:
- Регистрация, получение/удаления токена, смена пароля.
- Получение, создание, обновление, удаление рецептов.
- Получение одного или всех ингредиентов для рецептов. Создание только для admin.
- Получение одного или всех тэгов для рецептов. Создание только для admin.
- Добавление рецептов в избранное и их удаление из избранного.
- Добавление и удаление рецептов в/из списка покупок, а также скачивание списка покупок в pdf.
- Получение, создание, удаление подписки на авторов рецептов.


### Технологии
- Python3.10.6
- Django
- djangorestframework
- Nginx
- Gunicorn
- React
- Certbot
- Docker


### Как запустить проект локально с помощью Doker:

Клонировать репозиторий и перейти в него в терминале:

```
git clone git@github.com:TimofeiMedvedev/foodgram.git
```

Перейдите в корневую директорию пректа и создайте файл .env:

```
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
```

Запустите в корневой директории образы из файла Docker-compose:
```
docker-compose up -d --build
```

Примените миграции:

```
docker-compose exec backend python manage.py migrate
```

Соберите статику:

```
docker-compose exec backend python manage.py collectstatic --no-input
```

Скопируйте файлы статики для volume:

```
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/ 
```

Создайте суперпользователя:

```
docker-compose exec backend python manage.py createsuperuser
```

<br>

### Импорт данных из csv для наполнения базы:

В терминале наберите команду:

```
docker-compose exec backend python manage.py load_data_from_csv
```

В терминале отобразится результат импорта.<br>
Если какой-либо из файлов отсутствует, то он не будет импортирован.

Примеры файлов csv для наполнения базы находятся в папке data/*.csv:
- ingredients.csv - файл для заполнения таблицы ингредиентов.
<br>

Автор проекта:
<br>
Медведев Тимофей [Github](https://github.com/TimofeiMedvedev)

