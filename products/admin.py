from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Category, ProductReview


#class ProductImageTabular(admin.TabularInline):
 #   model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    #inlines = [ProductImageTabular]
    list_display = ("name", "sku", "flag", "quantity", "brand", "category", "price")
    list_filter = ("flag", "brand", "category", "price")
    search_fields = ("name", "desc", "subtite", "sku", "brand__name", "category__name")


admin.site.register(Product, ProductAdmin)
#admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Brand)
admin.site.register(Category)
