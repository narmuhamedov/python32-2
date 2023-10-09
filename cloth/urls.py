from django.urls import path
from . import views

urlpatterns = [
    path('man_cloth/', views.ManClothView.as_view(), name='man_cloth'),
    path('women_cloth/', views.WomenClothView.as_view(), name='women_cloth'),
    path('teen_cloth/', views.TeenagerClothView.as_view(), name='teen_cloth'),
    path('add-order/', views.AddOrder.as_view(), name='order'),
]