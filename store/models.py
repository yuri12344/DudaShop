from secrets import choice
from unicodedata import category
from django.db import models

class Category(models.Model):
    """Representation of category in the store"""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Representation of product in the store"""

    category =      models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name =          models.CharField(max_length=200, db_index=True)  
    slug =          models.SlugField(max_length=200, db_index=True)
    image =         models.ImageField(upload_to='static/%Y/%m/%d', blank=True)
    description =   models.TextField(blank=True)
    price =         models.DecimalField(max_digits=10, decimal_places=2)
    available =     models.BooleanField(default=True)
    created =       models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name