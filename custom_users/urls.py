from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="registrations"),
    path("login/", views.AuthLoginView.as_view(), name="login"),
    path("users/", views.UserListView.as_view(), name="user_list"),
]
