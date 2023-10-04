from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    pass