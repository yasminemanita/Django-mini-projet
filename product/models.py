from django.db import models

# Create your models here.

class Product(models.Model):
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")