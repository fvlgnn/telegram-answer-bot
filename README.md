# Telegram Answer Bot in Python Django
A Telegram Bot written in Python with Django Framework. Its main feature is to reply to messages by searching for keywords within them.

**This Bot works with [Webhooks](https://core.telegram.org/bots/api#setwebhook) method.** View [Telegram Bot API](https://core.telegram.org/bots/api) Documentation. 


## Virtual Environment

- `python3 -m venv venv`
- `source venv/bin/activate` (win `.\venv\Scripts\activate`)
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt`


## Project 

---

### Git

Clone this repo

- `git clone https://github.com/fvlgnn/omnia`


### Django (optional)

Use only remake project. Not use with git clone.

- `django-admin startproject bot .`
- `python manage.py startapp app`

---

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py collectstatic`

## Debug / Develop

- `python manage.py runserver`


## Deploy


### Self Hosting, Personal Cloud or VPS

Read [https://github.com/fvlgnn/setup-django-web-server](https://github.com/fvlgnn/setup-django-web-server)


### Hosting

[Heroku](https://www.heroku.com/), [PythonAnyWhere](https://eu.pythonanywhere.com), [DigitalOcean](https://www.digitalocean.com/).