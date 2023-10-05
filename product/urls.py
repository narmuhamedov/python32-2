from django.urls import path
from . import views

urlpatterns = [
    path("product_list/", views.ProductListView.as_view(), name="product"),
    path(
        "product_detail/<int:id>/", views.ProductDetailListView.as_view(), name="detail"
    ),
    path("eat_tags/", views.EatTagView.as_view(), name="eat"),
]
