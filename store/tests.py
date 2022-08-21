from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Category
import ipdb


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.category = Category.objects.create(
            name='Jeans',
            slug='jeans'
        )

    def test_it_has_information_fields(self):                   
        self.assertIsInstance(self.category.name, str)
        self.assertIsInstance(self.category.slug, str)

    def test_category_call_shows_name_and_are_string(self): 
        category_name = f"{self.category.name}"
        self.assertEquals(str(self.category.name), category_name)

    def test_creating_multiple_categories(self):
        shirts = Category()
        shirts.name = 'Shirts'
        shirts.slug = 'shirts'
        shirts.save()
        bottoms = Category()
        bottoms.name = 'Bottoms'
        bottoms.slug = 'bottoms'
        bottoms.save()
        self.assertEquals(Category.objects.count(), 3) # 3 categories in total
        self.assertEquals(Category.objects.get(name='Shirts'), shirts)
        self.assertEquals(Category.objects.get(name='Bottoms'), bottoms)
        self.assertEquals(Category.objects.get(slug='shirts'), shirts)
        self.assertEquals(Category.objects.get(slug='bottoms'), bottoms)


    def test_category_has_slug_field(self):
        self.assertIsInstance(self.category.slug, str)

    def test_category_has_name_field(self):
        self.assertIsInstance(self.category.name, str)


class CategoryRequestTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='user', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_can_create_categories(self):
        response = self.client.post('/api/v1/category/', data={'name': 'Shoes', 'slug': 'shoes'})
        obj = Category.objects.get(name='Shoes')
        self.assertEquals(obj.name, 'Shoes')    
        self.assertEquals(response.status_code, 201)

    def test_can_retrieve_categories(self):
        self.client.post('/api/v1/category/', data={'name': 'Shoes', 'slug': 'shoes'})
        self.client.post('/api/v1/category/', data={'name': 'Shirts', 'slug': 'shirts'})
        self.client.post('/api/v1/category/', data={'name': 'Shirt1s', 'slug': 'shirt1s'})
        
        response = self.client.get('/api/v1/category/')
        self.assertEquals(response.status_code, 200)
        self.assertGreater(len(response.data), 1)


    def test_can_retrieve_one_category(self):
        self.client.post('/api/v1/category/', data={'name': 'Cool boots', 'slug': 'cool-boots'})
        response = self.client.get('/api/v1/category/1/')
        self.assertEquals(response.status_code, 200)


    def test_can_delete_one_category(self):
        self.client.post('/api/v1/category/', data={'name': 'Cool boots', 'slug': 'cool-boots'})
        actual = Category.objects.count()
        response = self.client.delete('/api/v1/category/1/')
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Category.objects.count(), actual - 1)

