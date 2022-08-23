from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from store.models import Category


class CategoryRequestApiTest(APITestCase):
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

