from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length = 200, verbose_name = "نام سایت")
    site_url = models.CharField(max_length = 200, verbose_name = "دامنه ی سایت")
    address = models.CharField(max_length = 200, verbose_name = "آدرس سایت")
    phone = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "شماره تماس سایت")
    fax = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "فکس سایت")
    email = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "ایمیل سایت")
    copy_right = models.TextField(verbose_name = "تن کپی زایت سایت")
    about_us_text = models.TextField(verbose_name = "متن درباره ی ما")
    site_logo = models.ImageField(upload_to = 'images/site-setting/', verbose_name = "لوگو سایت")
    is_main_setting = models.BooleanField(verbose_name = "تنظیمات اصلی")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name