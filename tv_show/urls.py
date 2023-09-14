from django.urls import path
from . import views

urlpatterns = [
    path('film_list/', views.tv_show_view, name='films'),
    path('film_detail/<int:id>/', views.tv_show_detail_view, name='film_detail'),
]