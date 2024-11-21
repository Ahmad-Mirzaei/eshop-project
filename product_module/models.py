from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# test for git pull command
# category for products 
class ProductCategory(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    url_title = models.CharField(max_length = 300, verbose_name = "عنوان در url")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return f"({self.title} - {self.url_title})"



class ProductInformation(models.Model):
    color = models.CharField(max_length = 300, verbose_name = "رنگ")
    size = models.CharField(max_length = 300, blank = True, verbose_name = "سایز")

    class Meta:
        verbose_name = "اطلاعات تکمیلی"
        verbose_name_plural = "تمام اطلاعات تکمیلی"

    def __str__(self):
        return f"color : {self.color} - size : {self.size}"



class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, null = True, related_name = "products", verbose_name = "دسته بندی")
    product_information = models.OneToOneField(ProductInformation, on_delete = models.CASCADE, null = True, blank = True, related_name = "product_information", verbose_name = "اطلاعات تکمیلی")
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    price = models.IntegerField(verbose_name = "قیمت")
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)], default = 0, verbose_name = "امتیاز")
    short_description = models.CharField(max_length = 360, null = True, verbose_name = "توضیحات خلاصه")
    is_active = models.BooleanField(default = False, verbose_name = "وضعیت")
    # slug = models.SlugField(default = "", null = False, db_index = True, blank = True, editable = False)
    slug = models.SlugField(default = "", null = False, db_index = True, blank = True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return f"{self.title} ({self.price})"

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
