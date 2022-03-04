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

Clone this repo.

- `git clone https://github.com/fvlgnn/telegram-answer-bot`


### Django (optional)

Use only remake project. Don't use with git clone.

- `django-admin startproject bot .`
- `python manage.py startapp app`
- `python manage.py collectstatic`


## Configuration

- Copy or Rename `.env.example.file.txt` file in `.env`
- Edit `.env` file with your parameters


### Environment Parameters Description (`.env` file content's)

- `DEBUG` true/false be enable/disable debug mode
- `TELEGRAM_BOT_TOKEN` is alphanumericals token released of Telegram [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
- `SECRET_KEY` is alphanumericals string for django security
- `HOST` list of allowed hosts or DNS domains separated by space (Important `api.telegram.org`)
- `SQLITE_DB` true use SQLite, false use PostgreSQL, in this case configure PostgreSQL parameters
- If using PostgreSQL Database(`SQLITE_DB=false`)
    - `POSTGRESQL_NAME` is database name
    - `POSTGRESQL_USER` is username of database user enabled to use
    - `POSTGRESQL_PASS` is passoword of user
    - `POSTGRESQL_HOST` is database host name
    - `POSTGRESQL_PORT` is database port 


### Create Admin Django

- `python manage.py createsuperuser`


## Debug / Develop


### Check code and database migration

- `python manage.py makemigrations`
- `python manage.py migrate`

### Run Django Local Server

- `python manage.py runserver`


## Telegram Answer Bot Configuration

- Visit Admin page [http://127.0.0.1:8000/telegram-answer-bot-admin/](http://127.0.0.1:8000/telegram-answer-bot-admin/) or https://your-domain.net/telegram-answer-bot-admin/
- Using credential created by _manage.py createsuperuser_
- Configure Keyword and Answer

With Postman or other REST Client or by cURL, set the Telegram Bot for using [Webhooks](https://core.telegram.org/bots/api#setwebhook)


### Set Webhook

Method GET or POST `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook?url=https://your-domain.net/telegram-answer-bot/webhook`

**EDIT THIS:**

- `bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` is Telegram bot token api
- `https://your-domain.net` is your domain with valid SSL certificate (HTTPS)


If you haven't an HTTPS connection (with valid SSL certificate), must be created a self signed certificate and upload it on Telegram API Webhook.

**Curl example (edit token, domain and file)** 

```
curl --location --request POST 'https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook' \
--form 'url="https://your-domain.net/telegram-answer-bot/webhook"' \
--form 'certificate=@"/path/to/self-sign-public-key-certificate-file"'
```

With Postman use method `POST` and `body` as `form-data` with keys `url` value and `certificate` file. 

Read [https://core.telegram.org/bots/api#setwebhook](https://core.telegram.org/bots/api#setwebhook) and [https://core.telegram.org/bots/self-signed](https://core.telegram.org/bots/self-signed)


## Deploy


### Self Hosting, Personal Cloud or VPS

For deploy on custom host read [https://github.com/fvlgnn/setup-django-web-server](https://github.com/fvlgnn/setup-django-web-server)

It's very important that your host has an HTTPS connection (valid SSL encryption e.g. https://your-domain.net/) otherwise, a self-signed certificate must be created and used, view [Set Webhook](#set-webhook).


### Hosting

Read the documentation of the chosen service.

Advice [Heroku](https://www.heroku.com/), [PythonAnyWhere](https://eu.pythonanywhere.com), [DigitalOcean](https://www.digitalocean.com/).


----

## TODO

- [ ] Send Broadcast message by Django Admin page, using django signals. Environment `TELEGRAM_BOT_TOKEN` will be used for this.

