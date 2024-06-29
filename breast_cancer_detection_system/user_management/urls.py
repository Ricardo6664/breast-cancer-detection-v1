from django.urls import path
from user_management.views import index

app_name = 'user_management'

urlpatterns = [
    path('', index, name="index"),
]
