from django.test import TestCase
from store.models import Category


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

