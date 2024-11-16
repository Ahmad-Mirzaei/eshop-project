from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    price = models.IntegerField(verbose_name = "قیمت")
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)], default = 0, verbose_name = "امتیاز")
    short_description = models.CharField(max_length = 360, null = True, verbose_name = "توضیحات خلاصه")
    is_active = models.BooleanField(default = False, verbose_name = "وضعیت")

    def __str__(self):
        return f"{self.title} ({self.price})"

