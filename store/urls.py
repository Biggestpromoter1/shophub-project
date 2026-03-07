"""
This is how Django finds what functions (or classes) to use to handle
client requests. "Client" in this case is your frontend UI.
"""

from django.urls import path

from store import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path(
        "category/<slug:category_slug>/",
        views.product_list,
        name="product_list_by_category",
    ),
    path("product/<slug:slug>", views.product_detail, name="product_detail"),
    path("search/", views.search, name="search"),
]
