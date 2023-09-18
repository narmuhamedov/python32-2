from django.urls import path
from . import views

urlpatterns = [
    path('', views.tv_show_view, name='films'),
    path('film_detail/<int:id>/', views.tv_show_detail_view, name='film_detail'),
    path('film_detail/<int:id>/delete/', views.delete_tv_show_view, name='delete_film'),
    path('film_detail/<int:id>/update/', views.update_tv_show_view, name='update_film'),
    path('create_film/', views.add_tv_show_view, name='create_film'),
]