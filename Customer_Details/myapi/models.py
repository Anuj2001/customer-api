from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    bill = models.IntegerField(default=0)
    mob_no = models.CharField(max_length=13)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name