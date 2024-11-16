from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    price = models.IntegerField(verbose_name = "قیمت")


