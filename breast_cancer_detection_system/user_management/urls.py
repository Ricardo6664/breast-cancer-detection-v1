# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = "user_management"

urlpatterns = [
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="user_management/password_reset_form.html",
                                email_template_name="user_management/password_reset_email.html",
                                 success_url=reverse_lazy('user_management:password_reset_done')), name="password_reset"),
path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="user_management/password_reset_done.html"),
name="password_reset_done"),

    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="user_management/password_reset_confirm.html"),
    name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="user_management/password_reset_complete.html"),
    name="password_reset_complete"),
]
