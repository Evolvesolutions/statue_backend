# models.py
from django.db import models

class Statue(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='statues/')  # ✅ this must be ImageField

    def __str__(self):
        return self.name
    

# class Home_list(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     image = models.ImageField(upload_to='statue/')