from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from store.models import Product, Category
import ipdb

class ProductRequestApiTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        # Create one category and one product
        self.product = Product.objects.create(name='Category', category_id=1, price=10)
        self.category = Category.objects.create(name='jeans', slug='jeans')
        

    def test_can_add_products_to_cart_from_endpoint(self):
        res = self.client.post('/api/v1/cart/1', data={'quantity': 1})
        self.assertEqual(res.status_code, 200)

    def test_can_update_products_in_cart_from_endpoint(self):
        res = self.client.post('/api/v1/cart/1', data={'quantity': 1, 'override_quantity': 1})
        self.assertEqual(res.status_code, 200)

