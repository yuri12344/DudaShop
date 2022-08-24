from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class OrderEndPointTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_orders(self):
        response = self.client.get('/api/v1/order/')
        self.assertEqual(response.status_code, 200)
    
    def test_try_create_order_with_empty_cart(self):
        response = self.client.post('/api/v1/order/')
        message = eval(response.content)['message']
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message, "your cart is empty")
