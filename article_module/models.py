from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete = models.CASCADE, null = True, blank = True, verbose_name = "دسته بندی والد")
    title = models.CharField(max_length = 200, verbose_name = "عنوان دسته بندی")
    url_title = models.CharField(max_length = 300, unique = True, verbose_name = "عنوان در url")
    is_active = models.BooleanField(default = True, verbose_name = "فعال / غیرفعال")

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی های مقالات"

    def __str__(self):
        return self.title



