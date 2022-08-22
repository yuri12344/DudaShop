from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APITestCase
from store.models import Category, Product
from django.urls import reverse

import ipdb
import requests
class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.product = Product.objects.create(
            category=Category.objects.create(
                name='Jeans',
                slug='jeans'
            ),
            name = 'Calça',
            slug = 'calca',
            image = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            description = 'Calça jeans',
            price = '100.00',
            available = True
        )


    def test_it_has_information_fields(self):
        self.assertIsInstance(self.product.name, str)
        self.assertIsInstance(self.product.slug, str)
        self.assertIsInstance(self.product.description, str)
        self.assertIsInstance(self.product.price, str)
        self.assertIsInstance(self.product.available, bool)
        self.assertIsInstance(self.product.created, datetime)
        self.assertIsInstance(self.product.updated, datetime)

    def test_product_call_shows_name_and_are_string(self):
        product_name = f"{self.product.name}"
        self.assertEquals(str(self.product.name), product_name)


class ProductRequestApiTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        

    def test_product_list_request(self):
        self.client.post('/api/v1/category/', data={'name': 'Jeans', 'slug': 'jeans'})
        response = self.client.get('/api/v1/product/')
        self.assertEqual(response.status_code, 200)


    def test_product_create_request(self):
        self.client.post('/api/v1/product/', data={
            'category': '1',
            'name': 'Calça',
            'slug': 'calca',
            'image': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            'description': 'Calça jeans',
            'price': '100.00',
            'available': True
            }
        )
        response = self.client.get('/api/v1/product/')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_product_update_request(self):
        response = self.client.get(
            reverse('store:product-list')
        )
        self.assertEqual(response.status_code, 200)
    # TO DO - Solve problem with reverse