from django.shortcuts import render
from store.models import Product

def home(request):
    """Homepage with featured products"""

    featured_products = Product.objects.filter(available=True)[:8]
    context = {
        "featured_products": featured_products,
        "title": "Welcome to ShopHub"
    }
    return render(request, "store/home.html", context)
