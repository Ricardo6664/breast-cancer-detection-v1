from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
import boto3
import os

client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("region_name"),
)


def register(request):
    if request.method == "GET":
        return render(request, "user_management/register.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()
        email = User.objects.filter(email=email).first()

        if user:
            return HttpResponse("User already exists")

        if email:
            return HttpResponse("Email already exists")
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        client.put_object(Bucket=os.getenv("bucket_name"), Key=f"{username}/")

        return HttpResponse("User registered successfully")


def login(request):
    if request.method == "GET":
        return render(request, "user_management/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("core:home")
        else:
            return HttpResponse("Invalid credentials")
