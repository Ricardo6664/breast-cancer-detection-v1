from django.urls import path
from . import views

app_name = "user_management"

urlpatterns = [
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
]
