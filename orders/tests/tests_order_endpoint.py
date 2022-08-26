from email import header
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class CreateTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
       
        # Login
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key) 
        # Create category
        self.client.post('/api/v1/category/', {'name': 'jeans', 'slug': 'jeans'}) # Create category
        # Create product
        self.client.post('/api/v1/product/', { "category": "1","name": "Calça","slug": "calca","description": "Calça jeans","price": "100.00","available": 1  })
        # Add product to the cart
        self.client.post('/api/v1/cart/1', data={'quantity': '3'}) # Add to cart


    def test_can_check_create_order(self):
        order_res = self.client.post('/api/v1/order/' , data={
	        "first_name": "Yuri",
	        "last_name": "Caetano",
	        "email": "yuuri.caetano@gmail.com",
	        "address": "Rua Henriqe",
	        "postal_code": "83060460",
	        "city": "Sao Jose dos pinhais"
        })
        total = eval(order_res.content)['total_cost']
        self.assertEqual(total, 300)
        self.assertEqual(order_res.status_code, 201)
    
   