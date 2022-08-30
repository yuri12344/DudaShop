from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from cart.cart import Cart
from store.models import Product, Category


class OrderEndPointTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.product = Product.objects.create(name='Category', category_id=1, price=10)
        self.category = Category.objects.create(name='jeans', slug='jeans')

    def test_get_orders(self):
        response = self.client.get('/api/v1/order/')
        self.assertEqual(response.status_code, 200)
    
    def test_try_cant_create_order_with_empty_cart(self):
        response = self.client.post('/api/v1/order/')
        message = eval(response.content)['message']
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message, "your cart is empty")


    def test_get_total_cost_of_my_order(self):
        cart = Cart(self.client)
        product = self.product
        cart.add(product=product, quantity=10)
        
        #self.assertEqual(, 100)

