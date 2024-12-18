from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length = 200, verbose_name = "نام سایت")
    site_url = models.CharField(max_length = 200, verbose_name = "دامنه ی سایت")
    address = models.CharField(max_length = 200, verbose_name = "آدرس ")
    phone = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "شماره تماس ")
    fax = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "فکس ")
    email = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "ایمیل ")
    copy_right = models.TextField(verbose_name = "متن کپی رایت ")
    about_us_text = models.TextField(verbose_name = "متن درباره ی ما")
    site_logo = models.ImageField(upload_to = 'images/site-setting/', verbose_name = "لوگو سایت")
    is_main_setting = models.BooleanField(verbose_name = "تنظیمات اصلی")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "عنوان")

    class Meta:
        verbose_name = "دسته بندی لینک های فوتر"
        verbose_name_plural = "دسته بندی های لینک های فوتر"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "عنوان")
    url = models.URLField(max_length = 500, verbose_name = "لینک")
    footer_link_box = models.ForeignKey(to = FooterLinkBox, on_delete = models.CASCADE, verbose_name = "دسته بندی")

    class Meta:
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک های فوتر"

    def __str__(self):
        return self.title