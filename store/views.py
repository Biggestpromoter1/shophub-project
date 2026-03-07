from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Product, Category


def home(request):
    """Homepage with featured products"""
    featured_products = Product.objects.filter(
        available=True)[:8]  # Get 8 latest available products

    context = {"featured_products": featured_products, "title": "Welcome to ShopHub"}
    return render(request, "store/home.html", context)


def product_list(request, category_slug=None):
    """List all products or products by category with pagination and sorting"""
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.annotate(product_count=Count("products"))

    # Sorting
    sort_by = request.GET.get("sort", "-created_at")
    valid_sorts = ["price", "-price", "name", "-name", "-created_at"]
    if sort_by in valid_sorts:
        products = products.order_by(sort_by)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Pagination
    # Task: research pagination, understand what it is and why it is sometimes used
    paginator = Paginator(products, 6)  # 6 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "products": page_obj,
        "categories": categories,
        "current_sort": sort_by,
        "title": f"{category.name} Products" if category else "All Products",
    }
    return render(request, "store/product_list.html", context)


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug, available=True)

    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category, available=True
    ).exclude(id=product.id)[:4]

    context = {
        "product": product,
        "related_products": related_products,
        "title": product.name,
    }
    return render(request, "store/product_detail.html", context)


# Added a search function to handle database queries
def search(request):
    # added a default (""), so the app gracefully handles when there's no query param
    query = request.GET.get("q", "")
    # better to name your variables well, so you have an idea what it returns or what it's for
    products_list = Product.objects.filter(name__icontains=query, available=True)

    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "store/search.html",
        {
            "products": page_obj,
            "query": query,
        },
    )
