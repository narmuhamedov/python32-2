from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models


class ProductListView(ListView):
    # queryset = models.Product.objects.all()
    queryset = models.Product.objects.filter().order_by("-id")
    template_name = "products/product_list.html"

    def get_queryset(self):
        return models.Product.objects.filter().order_by("-id")
        # return models.Product.objects.all()


class EatTagView(ListView):
    queryset = models.Product.objects.filter(tags__name="food")
    template_name = "products/eat_tags.html"

    def get_queryset(self):
        return models.Product.objects.filter(tags__name="food")


class ProductDetailListView(DetailView):
    template_name = "products/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)
