from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user_management'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
        template_name='user_management/form.html'
        ),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
]
