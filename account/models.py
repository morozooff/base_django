from django.db import models

class Account(models.Model):
     condition = models.IntegerField(default=0)
     premium_status = models.BooleanField(default=False)
