from django.db import models

from user_api.models import MyUser, Address

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.name
    
class OrderedItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.name
    
ORDER_STATUS_CHOICES = [
    ('pending', 'pending'),
    ('completed', 'completed'),
]
    
class Order(models.Model):
    item = models.ForeignKey(OrderedItem, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES)
    transaction_id = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    