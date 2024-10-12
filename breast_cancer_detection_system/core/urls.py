from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("upload_img/", views.upload_img, name="upload_img"),
    path("img_save/", views.image_save, name="image_save"),
]
