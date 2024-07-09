# Создание новостного веб-приложения

## Requirements
asgiref==3.7.2

Django==4.2.7

django-taggit==5.0.1

Pillow==10.1.0

sqlparse==0.4.4

typing_extensions==4.8.0

tzdata==2023.3

## Запуск проекта
pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Обзор веб-приложения
После запуска проекта зарегистрируем пользователя. Перейдем на страницу /news/register/ и введем данные:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/cda85270-10a5-460d-a67b-d69d7eeb74c7)

После успешной регистрации осуществляется переход на главную страницу /news/, где будет возможность выйти из аккаунта через Logout:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/4370b020-13a0-49ca-a68b-8796917a8592)

Войти в аккаунт можно через страницу /news/login/: 

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/fc5631a5-9f16-4280-b9ef-5eebff7ea30a)

Аналогичным образом пользователь перейдет на главную страницу:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/57657d4c-93a3-43db-a549-add94144a291)

Создание новостей. Данная опция есть только у администратора. Войдем в аккаунт и создадим несколько записей:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/7fd48a14-df1c-4e15-af80-d4c8634c6c22)

На главной странице отображаются пять последних новостей:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/51a30ff4-8ab5-4d21-a601-d2bf2f1f5899)

Пример новостной записи:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/1e3db9c7-3e24-42f3-abcc-9a9d38728480)

Присутствует возможность редактирования записи, если это твоя новость. Администратор может изменять все записи:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/1540c7ac-79b5-4395-8128-55ff46768f58)

В ином случае, получим сообщение:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/6a8c4e9e-d1ab-451f-a909-909df290969e)

Каждая новость относится к определенной категории. Категория «unimportant»:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/90b4c94e-89c8-43b6-b47b-a1340d4439dc)

Категория «important»:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/8c3459b2-33cc-4264-8843-0f4337567afe)

Административная панель Django:

![image](https://github.com/ArtemK64/python-django-tasks/assets/79468247/e01e1ffd-efd9-4301-9202-3fce3ec25cb9)
