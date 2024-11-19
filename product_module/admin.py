from django.contrib import admin

from . import models
# Register your models here.

# step 1
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']  # or ("slug", )
    prepopulated_fields = {'slug': ["title"]}



# step 2
# admin.site.register(models.Product, ProductAdmin)