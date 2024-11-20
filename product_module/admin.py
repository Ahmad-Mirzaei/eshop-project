from django.contrib import admin

from . import models
# Register your models here.

# step 1
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']  # or ("slug", )
    prepopulated_fields = {'slug': ["title"]}
    list_display = ["title", "price", "rating", "is_active"]
    list_filter = ["rating", "is_active"]
    list_editable = ["rating", "is_active"]

# step 2
# admin.site.register(models.Product, ProductAdmin)
# ----------------------------------------------------------------------------------------------------------------------
# test for git push -u origin master
# test for git push