from django.db import models

class Category(models.Model):
    """Representation of category in the store"""

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

