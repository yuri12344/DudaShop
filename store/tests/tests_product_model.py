from datetime import datetime
from django.test import TestCase
from store.models import Category, Product

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

