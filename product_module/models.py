from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


# test for git pull command
# category for products 
class ProductCategory(models.Model):
    title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان")
    url_title = models.CharField(max_length = 300, db_index = True, verbose_name = "عنوان در url")
    is_active = models.BooleanField(verbose_name = "فعال / غیرفعال")
    is_delete = models.BooleanField(verbose_name ="حذف شده / نشده")


    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return f"({self.title} - {self.url_title})"
# ----------------------------------------------------------------------------------------------------------------------

class ProductBrand(models.Model):
    title = models.CharField(max_length = 300, db_index = True, verbose_name = "نام برند")
    is_active = models.BooleanField(verbose_name = "فعال / غیرفعال")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return f"{self.title} {self.is_active}"
# ----------------------------------------------------------------------------------------------------------------------
class Product(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    category = models.ManyToManyField(ProductCategory, related_name = "product_categories", verbose_name = "دسته بندی ها")
    brand = models.ForeignKey(ProductBrand, on_delete = models.CASCADE, null = True, blank = True, verbose_name = "برند")
    price = models.IntegerField(verbose_name = "قیمت")
    short_description = models.CharField(max_length = 360, null = True, db_index = True, verbose_name = "توضیحات کوتاه")
    description = models.TextField(db_index = True, verbose_name = "توضیحات اصلی")
    slug = models.SlugField(max_length = 200, default = "", null = False, db_index = True, blank = True, unique = True)
    is_active = models.BooleanField(default = False, verbose_name = "فعال / غیرفعال")
    is_delete = models.BooleanField(verbose_name = "حذف شده / نشده")

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

# ----------------------------------------------------------------------------------------------------------------------

class ProductTag(models.Model):
    caption = models.CharField(max_length = 300, db_index = True, verbose_name = "برچسپ")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_tags", verbose_name = "")

    class Meta:
        verbose_name = "برچسپ محصول"
        verbose_name_plural = "برچسپ های محصولات"

    def __str__(self):
        return self.caption