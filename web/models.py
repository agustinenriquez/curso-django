from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name