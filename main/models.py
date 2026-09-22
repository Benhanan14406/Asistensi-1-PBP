from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def is_available(self):
        return self.stock > 0

    def is_low_stock(self):
        return 1 <= self.stock <= 3
