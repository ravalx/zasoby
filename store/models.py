from django.db import models



class Owner(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.first_name+' '+self.last_name

class Nr_ST(models.Model):
    nr_product = models.CharField(max_length = 15, unique=True)
    name_product = models.CharField(max_length = 100)
    date_of_acceptance = models.DateField()
    value_product = models.PositiveIntegerField(null=True)
    user = models.CharField(max_length = 50)
    room = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to = 'img', null=True)
    note = models.TextField()
    owner = models.ForeignKey('Owner')

    def __str__(self):
        return self.name_product

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

    def __str__(self):
        return [self.nr_product, self.name_product, ]
