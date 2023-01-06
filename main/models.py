from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    link = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
