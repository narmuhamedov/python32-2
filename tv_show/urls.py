from django.urls import path
from . import views

urlpatterns = [
    path("", views.TvShowView.as_view(), name="films"),
    # path('', views.tv_show_view, name='films'),
    path("film_detail/<int:id>/", views.TvShowDetailView.as_view(), name="film_detail"),
    path(
        "film_detail/<int:id>/delete/",
        views.DeleteTvShowView.as_view(),
        name="delete_film",
    ),
    path(
        "film_detail/<int:id>/update/",
        views.UpdateTvShowView.as_view(),
        name="update_film",
    ),
    path("create_film/", views.AddTvShowView.as_view(), name="create_film"),
    path("search/", views.Search.as_view(), name="search"),
]
