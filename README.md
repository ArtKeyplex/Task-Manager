# Task-Manager
Сайт, позволяющий пользователям управлять своими делами, а также вести счет времени, потраченное на различные дела (Например, сколько всего времени человек читает)


Стек технологий
----------
* Python 3.8
* Django 2.2 
* Pytest
* SQLite3
* CSS
* HTML

Установка проекта из репозитория
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:ArtKeyplex/Task-Manager.git

cd Task-Manager
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv

source venv/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd todo

python3 manage.py migrate
```
5. Запустить проект (в режиме сервера Django):
```bash
python3 manage.py runserver
```
