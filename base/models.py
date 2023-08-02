from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    home_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
