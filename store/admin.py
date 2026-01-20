from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin interface"""

    list_display = ["name", "created_at"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin interface"""

    list_display = [
        "name",
        "category",
        "price",
        "stock",
        "available",
        "created_at",
    ]
    list_filter = ["available", "category", "created_at"]
    search_fields = ["name", "description"]
