from django.contrib import admin

from . import models
# Register your models here.

# step 1
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']  # or ("slug", )
    prepopulated_fields = {'slug': ["title"]}
    list_display = ["category", "title", "price", "rating", "is_active", "product_information"]
    list_filter = ["rating", "is_active"]
    list_editable = ["rating", "is_active"]

# step 2
# admin.site.register(models.Product, ProductAdmin)
# ----------------------------------------------------------------------------------------------------------------------
# test for git push -u origin master
# test for git push

@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "url_title"]
# admin.site.register(models.ProductCategory)


@admin.register(models.ProductInformation)
class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ["color", "size"]


@admin.register(models.ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["tag", ]