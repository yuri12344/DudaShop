# Duda Shop - Online Clothing Store

This is the backend for the Duda Shop. Made with Django and Python, fast and escalable.

To start project you will need to have virtual env with Python3 at least

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone git@github.com:yuri12344/DudaShop.git
$ cd duda-shop
```


<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ python3 -m venv venv_prod
$ source venv_prod/bin/activate
$ pip3 install -r requirements/develop.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ python -m venv_dev
$ .\venv_dev\Scripts\activate
$ pip3 install -r \requirements\develop.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />
