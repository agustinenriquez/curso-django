from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
