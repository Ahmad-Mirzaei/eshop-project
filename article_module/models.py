from django.db import models
from account_module.models import User
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



class Article(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "عنوان مقاله")
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True, editable = False, verbose_name = "نویسنده")
    slug = models.SlugField(max_length = 400, db_index = True, allow_unicode = True, verbose_name = "عنوان در url")
    image = models.ImageField(upload_to = 'images/articles', verbose_name = "تصویر مقاله")
    short_description = models.TextField(verbose_name = "توضیحات کوتاه")
    text = models.TextField(verbose_name = "متن مقاله")
    is_active = models.BooleanField(default = True, verbose_name = "فعال / غیرفعال")
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name = "دسته بندی ها")
    create_date = models.DateTimeField(auto_now_add = True, editable = False, verbose_name = "تاریخ ثبت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title


class ArticlesComment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "مقاله")
    parent = models.ForeignKey('ArticlesComment', on_delete = models.CASCADE, null =True, blank = True, verbose_name = "والد")
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "کاربر")
    create_date = models.DateTimeField(auto_now_add = True, verbose_name = "تاریخ ثبت")
    text = models.TextField(verbose_name = "متن نظر")

    class Meta:
        verbose_name = "نظر مقاله"
        verbose_name_plural = "نظرات مقالات"

    def __str__(self):
        return f"{self.user}"