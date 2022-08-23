from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


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

    # TODO
    # Create more tests