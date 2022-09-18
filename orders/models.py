from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from account.models import Account
from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    release_date = models.DateField(default='2001-09-21')
    stock_location = models.CharField(max_length=255, default='Ozon stock')
    is_on_stock = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
