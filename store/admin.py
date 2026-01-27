from django.contrib import admin
from .models import Product, Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "price",
        "stock",
        "available",
        "created_at",
    )
    list_filter = ("available", "category", "brand", "created_at")
    search_fields = ("name", "description")
