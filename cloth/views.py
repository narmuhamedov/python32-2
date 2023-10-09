from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms

class ManClothView(ListView):
    queryset = models.Product.objects.filter(tags__name="мужское")
    template_name = "cloth/man_cloth.html"

    def get_queryset(self):
        return models.Product.objects.filter(tags__name="мужское")

class ManClothDetailView(DetailView):
    template_name = 'cloth/man_cloth_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)

#---------------------------------------------

class WomenClothView(ListView):
    queryset = models.Product.objects.filter(tags__name="женское")
    template_name = "cloth/women_cloth.html"

    def get_queryset(self):
        return models.Product.objects.filter(tags__name="женское")


class WomenClothDetailView(DetailView):
    template_name = 'cloth/women_cloth_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)


class TeenagerClothView(ListView):
    queryset = models.Product.objects.filter(tags__name="подросковое")
    template_name = "cloth/teen_cloth.html"

    def get_queryset(self):
        return models.Product.objects.filter(tags__name="подросковое")


class TeenagerClothDetailView(DetailView):
    template_name = 'cloth/teen_cloth_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)

#------------------------------------
class AddOrder(CreateView):
    template_name = "cloth/order.html"
    form_class = forms.OrderForm
    queryset = models.Product.objects.all()
    success_url = "http://127.0.0.1:8000/admin/cloth/order/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddOrder, self).form_valid(form=form)

