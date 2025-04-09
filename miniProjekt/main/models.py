from django.db import models


class Order(models.Model):

    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    telephone_number = models.DecimalField(max_digits=15, decimal_places=2)
    message = models.TextField()
    email = models.EmailField()
