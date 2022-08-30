from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from store.models import Product, Category

class CartEndPointTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # Create one category and one product
        self.product = Product.objects.create(name='Category', category_id=1, price=10)
        self.category = Category.objects.create(name='jeans', slug='jeans')


    def test_can_add_product(self):
        response = self.client.post(f'/api/v1/cart/{self.product.id}', {'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(eval(response.content)), 1)

    def test_can_update_product_quantity(self):
        response = self.client.post(f'/api/v1/cart/{self.product.id}', {'quantity': 10})

        response = self.client.put(f'/api/v1/cart/{self.product.id}', {'quantity': 5})
        self.assertEqual(response.status_code, 200)
        quantity = eval(response.content)[str(self.product.id)]['quantity']
        self.assertEqual(quantity, 5)


    def test_cant_add_quantity_as_string_character(self):
        response = self.client.post(f'/api/v1/cart/{self.product.id}', {'quantity': 'testing if are able to add quantity as any text'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(eval(response.content)), 0) # eval because return is b'{}' and 0 Because the response is empty.
    

    def test_can_add_quantity_as_integer(self):
        response = self.client.post(f'/api/v1/cart/{self.product.id}', {'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(eval(response.content)), 1) # Because the response is cart with product.


    def test_can_add_quantity_as_number_string(self):
        response = self.client.post(f'/api/v1/cart/{self.product.id}', {'quantity': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(eval(response.content)), 1) 