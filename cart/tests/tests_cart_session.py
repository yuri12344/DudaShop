from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from cart.cart import Cart
from store.models import Product, Category


class CartFunctionalityTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # Create one category and one product
        self.product = Product.objects.create(name='Category', category_id=1, price=10)
        self.category = Category.objects.create(name='jeans', slug='jeans')


    def test_add_product_to_cart(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        self.assertEqual(cart.cart[str(product.id)]['quantity'], 1)


    def test_update_product_in_cart(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        cart.add_or_update(product=product, quantity=2)
        self.assertEqual(cart.cart[str(product.id)]['quantity'], 3) # 3 Because the first test add 1 product and the second test add 2 products.


    def test_remove_product_from_cart(self):
        cart = Cart(self.client) # Create a new cart
        product = self.product
        cart.add_or_update(product=product, quantity=1) # {'1': {'quantity': 1, 'price': '10'}}
        cart.remove(product=product) # {}
        self.assertEqual(cart.cart, {})


    def test_get_cart_total_price(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        self.assertEqual(cart.get_total_price(), 10) # 10 because self.product has price 10.


    def test_get_cart_total_quantity(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        self.assertEqual(cart.get_total_quantity(), 1)


    def test_get_cart_total_quantity_when_cart_is_empty(self):
        cart = Cart(self.client)
        self.assertEqual(cart.get_total_quantity(), 0)


    def test_get_cart_total_quantity_when_cart_is_not_empty(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        self.assertEqual(cart.get_total_quantity(), 1)

    
    def test_get_cart_total_quantity_when_cart_is_not_empty_and_there_are_more_products_than_one(self):
        cart = Cart(self.client)
        product = self.product
        cart.add_or_update(product=product, quantity=1)
        cart.add_or_update(product=product, quantity=2)
        self.assertEqual(cart.get_total_quantity(), 3)
