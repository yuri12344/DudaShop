# Duda Shop Online Clothing Store

This is the backend for the Duda Shop. Made with Django and Python, fast and scalable.

To start the project you will need to have at least a virtual env with Python3

# Diagrama de relacionamentos
https://drive.google.com/file/d/1GO0PJgiNuYH_Xnj6uaUspSXzESdKm4Ji/view?usp=sharing

# Fluxo arquitetura do projeto
https://whimsical.com/how-duda-shop-is-build-KSHNtQjmo5HG2CLEjaNsfY

# Projeto online
http://dudashop-api.ddns.net/admin/

u: dudashop
s: dudashop123


## ✨ How to use it

> Download the code 

```bash
$ # Get the repository
$ git clone git@github.com:yuri12344/DudaShop.git
$ cd duda-shop
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
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

base_url = "http://dudashop-api.ddns.net/api/v1/"


# Listar produtos
"http://dudashop-api.ddns.net/api/v1/product"


# Listar categorias
"http://dudashop-api.ddns.net/api/v1/category"


# Listar produtos da categoria
"http://dudashop-api.ddns.net/api/v1/category/{CATEGORY_ID}/products/"


# Adicionar produto ao carrinho
Method: POST
"http://dudashop-api.ddns.net/api/v1/cart/add/{PRODUCT_ID}"
body = {
	"quantity": 1
}


# Listar produtos do carrinho 
Method: POST

"http://dudashop-api.ddns.net/api/v1/cart"


# Atualizar o carrinho
Method: PUT

"http://dudashop-api.ddns.net/api/v1/cart/update/{PRODUCT_ID}"
body = {
	"quantity": 1
}
 at least
# Exclui 1 produto do carrinho
Method: DELETE

"http://dudashop-api.ddns.net/api/v1/cart/delete/{PRODUCT_ID}"


# Limpar carrinho
Method: DELETE

"http://dudashop-api.ddns.net/api/v1/cart/"


# Criar uma ordem
Method: POST

"http://dudashop-api.ddns.net/api/v1/order"

body = {
	"first_name": "Yuri",
	"last_name": "Caetano",
	"email": "yuuri.caetano@gmail.com",
	"address": "Rua Henriqe",
	"postal_code": "83060460",
	"city": "Sao Jose dos pinhais"
}

# Listar todas as ordens
Method: GET

"http://dudashop-api.ddns.net/api/v1/order"