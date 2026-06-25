from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    """Homepage with featured products"""
    featured_products = Product.objects.filter(
        available=True
    )[:8]  # Get 8 latest available products
    
    context = {
        'featured_products': featured_products,
        'title': 'Welcome to ShopHub'
    }
    return render(request, 'store/home.html', context)


def product_list(request, category_slug=None):
    """List all products or products by category"""
    category = None
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
        'title': f'{category.name} Products' if category else 'All Products'
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(
        Product, 
        slug=slug, 
        available=True
    )
    
    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
        'title': product.name
    }
    return render(request, 'store/product_detail.html', context)
def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)

    return render(request, 'store/search.html', {
        'products': products,
        'query': query,
    })