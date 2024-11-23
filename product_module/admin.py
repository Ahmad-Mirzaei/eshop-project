from django.contrib import admin

from . import models
# Register your models here.

# step 1
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["category", "is_active"]
    list_display = ["title", "price", "is_active", "is_delete", "brand"]
    list_editable = ["is_active", "price"]
    # prepopulated_fields = {'slug': ["title"]}

# step 2
# admin.site.register(models.Product, ProductAdmin)
# ----------------------------------------------------------------------------------------------------------------------
# test for git push -u origin master
# test for git push

@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "url_title", "is_active"]
# admin.site.register(models.ProductCategory)

@admin.register(models.ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["caption", ]


# @admin.register(models.ProductBrand)
# class ProductBrandAdmin(admin.ModelAdmin):
#     list_display = ["title"]

admin.site.register(models.ProductBrand)