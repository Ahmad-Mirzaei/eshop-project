from django.db import models
import datetime

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length = 300, verbose_name = "عنوان")
    email = models.EmailField(max_length = 300, verbose_name = "ایمیل")
    full_name = models.CharField(max_length = 300, verbose_name = "نام و نام حانوادگی")
    message = models.TextField(verbose_name = "متن تماس با ما")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "تاریخ ایجاد")
    response = models.TextField(null = True, blank = True, verbose_name = "متن پاسخ تماس با ما")
    is_read_by_admin = models.BooleanField(verbose_name = "خوانده شده توسط ادمین")  # default = False


    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "لیست تماس با ما"

    def __str__(self):
        return self.title

# ----------------------------------------------------------------------------------------------------------------------
