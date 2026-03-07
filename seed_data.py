"""
This is a script to populate the DB. You sometimes might want to do this
in development, so you have a better view of how the data looks like and
how your app works with it.
"""

import os
import django
import random

from django.utils.text import slugify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shophub.settings")
django.setup()

from store.models import Category, Brand, Product


def run():
    # Add some Brands
    brands = ["Apple", "Samsung", "Sony", "LG", "Dell", "HP", "Nike", "Adidas"]
    for name in brands:
        Brand.objects.get_or_create(name=name, defaults={"slug": slugify(name)})

    # Make sure we have some categories
    categories = ["Electronics", "Computing", "Fashion", "Home & Garden"]
    for name in categories:
        Category.objects.get_or_create(name=name, defaults={"slug": slugify(name)})

    # Add 5+ products
    cat_objs = list(Category.objects.all())
    brand_objs = list(Brand.objects.all())

    products_to_add = [
        {"name": "iPhone 15 Pro", "price": 1200000.00, "stock": 10},
        {"name": "Samsung Galaxy S24 Ultra", "price": 1400000.00, "stock": 5},
        {"name": "Sony WH-1000XM5", "price": 350000.00, "stock": 15},
        {"name": "Dell XPS 15", "price": 1800000.00, "stock": 3},
        {"name": 'LG OLED TV 65"', "price": 2200000.00, "stock": 2},
        {"name": "Nike Air Max 270", "price": 85000.00, "stock": 20},
        {"name": "Adidas Ultraboost", "price": 95000.00, "stock": 12},
    ]

    for prod in products_to_add:
        name = prod["name"]
        slug = slugify(name)
        category = random.choice(cat_objs)
        brand = random.choice(brand_objs)

        # Avoid duplication if possible or just update
        Product.objects.get_or_create(
            name=name,
            defaults={
                "slug": slug,
                "description": f"This is a great {name}. High quality and durable.",
                "price": prod["price"],
                "stock": prod["stock"],
                "category": category,
                "brand": brand,
                "available": True,
            },
        )

    print("Data added successfully!")


if __name__ == "__main__":
    run()
