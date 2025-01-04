from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.FooterLink, FooterLinkAdmin)
