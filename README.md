# Telegram Answer Bot in Python Django
A Telegram Bot written in Python with Django Framework. Its main feature is to reply to messages by searching for keywords within them.

**This Bot works with [Webhooks](https://core.telegram.org/bots/api#setwebhook) method.** View [Telegram Bot API](https://core.telegram.org/bots/api) Documentation. 


## Virtual Environment

- `python3 -m venv venv`
- `source venv/bin/activate` (win `.\venv\Scripts\activate`)
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt`


## Project 


### Git

Clone this repo

- `git clone https://github.com/fvlgnn/telegram-answer-bot`


### Django (optional)

Use only remake project. Not use with git clone.

- `django-admin startproject bot .`
- `python manage.py startapp app`

---

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py collectstatic`


## Configuration

- Copy or Rename `.env.example.file.txt` file in `.env`
- Edit `.env` file with your parameters


### Environment Parameters Description (`.env` file content's)

- `DEBUG` true/false be enable/disable debug mode
- `TELEGRAM_BOT_API` is alphanumericals string released of Telegram [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
- `SECRET_KEY` is alphanumericals string for django security
- `HOST` list of allowed hosts or DNS domains separated by space
- `SQLITE_DB` true use SQLite, false use PostgreSQL, in this case configure PostgreSQL parameters
- If using PostgreSQL Database(`SQLITE_DB=false`)
    - `POSTGRESQL_NAME` is database name
    - `POSTGRESQL_USER` is username of database user enabled to use
    - `POSTGRESQL_PASS` is passoword of user
    - `POSTGRESQL_HOST` is database host name
    - `POSTGRESQL_PORT` is database port 


## Debug / Develop

- `python manage.py runserver`


## Deploy


### Self Hosting, Personal Cloud or VPS

Read [https://github.com/fvlgnn/setup-django-web-server](https://github.com/fvlgnn/setup-django-web-server)


### Hosting

Read the documentation of the chosen service .

Advice [Heroku](https://www.heroku.com/), [PythonAnyWhere](https://eu.pythonanywhere.com), [DigitalOcean](https://www.digitalocean.com/).

