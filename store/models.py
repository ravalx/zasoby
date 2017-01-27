from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)

class Nr_ST(models.Model):
    nr_product = models.CharField(max_length = 15)
    name_product = models.CharField(max_length = 100)
    date_of_acceptance = models.DateField()
    value_product = models.PositiveIntegerField()
    user = models.CharField(max_length = 50)
    room = models.CharField(max_length = 20)
    photo = models.ImageField()
    note = models.TextField()
    owner = models.ForeignKey('Owner')

class Nr_STC(models.Model):
    nr_product = models.CharField(max_length = 15)
    name_product = models.CharField(max_length = 100)
    date_of_acceptance = models.DateField()
    value_product = models.PositiveIntegerField()
    user = models.CharField(max_length = 50)
    room = models.CharField(max_length = 20)
    photo = models.ImageField()
    note = models.TextField()
    nr_st = models.ForeignKey('Nr_ST', on_delete=models.CASCADE)
