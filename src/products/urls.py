from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    dynamic_product_detail_view,
    product_delete_view,
    product_list_view,
)

app_name = "products"
urlpatterns = [
    path("", product_detail_view, name="product"),
    path("/list", product_list_view, name="product_list"),
    path("/create", product_create_view, name="create"),
    path("/<int:id>", dynamic_product_detail_view, name="dynamic_product"),
    path("/delete/<int:id>", product_delete_view, name="delete"),
]
