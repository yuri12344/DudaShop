from email import header
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

import ipdb

class CreateTest(APITestCase):
    # def setUp(self):
    #    user = User.objects.create_superuser(username='user', password='password')
    #    token = Token.objects.create(user=user)
    #    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


    def test_can_check_ifok(self):
        client = APIClient()
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        client.post('/api/v1/category/', {'name': 'jeans', 'slug': 'jeans'}) # Create category

        client.post('/api/v1/product/', {
            "category": "1",
            "name": "Calça",
            "slug": "calca",
            "description": "Calça jeans",
            "price": "100.00",
            "available": 1  
        })

        client.post('/api/v1/cart/1', data={'quantity': '3'})
        order_res = client.post('/api/v1/order/' , data={
	        "first_name": "Yuri",
	        "last_name": "Caetano",
	        "email": "yuuri.caetano@gmail.com",
	        "address": "Rua Henriqe",
	        "postal_code": "83060460",
	        "city": "Sao Jose dos pinhais"
        })
        total = eval(order_res.content)['total_cost']

        self.assertEqual(total, 300)

"""
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from cart.cart import Cart
from store.models import Product, Category
import ipdb

class OrderEndPointTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.product = Product.objects.create(name='Category', category_id=1, price=10)
        self.category = Category.objects.create(name='jeans', slug='jeans')
        self.client.cart = Cart(self.client)


    def test_get_orders(self):
        response = self.client.get('/api/v1/order/')
        self.assertEqual(response.status_code, 200)
    
    def test_try_cant_create_order_with_empty_cart(self):
        response = self.client.post('/api/v1/order/')
        message = eval(response.content)['message']
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message, "your cart is empty")


    def test_get_total_cost_of_my_order(self):
        res = self.client.post('/api/v1/cart/21', data={'quantity': 3})
        response = self.client.post('/api/v1/order/', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@gmail.com',
            'address': 'Street 407',
            'postal_code': '',
            'city': '',
            }
        )
        ipdb.set_trace()
        #self.assertEqual(, 100)

"""