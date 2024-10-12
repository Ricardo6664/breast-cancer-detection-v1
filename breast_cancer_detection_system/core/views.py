from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import boto3
import os

client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("region_name"),
)

s3 = boto3.resource(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("region_name"),
)


@login_required
def home(request):
    return render(request, "core/initial_page.html")


@login_required
def upload_img(request):
    return render(request, "core/upload_image.html")


@login_required
def image_save(request):
    if request.method == "GET":
        return render(request, "core/image_save.html")
    elif request.method == "POST":
        try:
            name = str(request.user.username)
            response = s3.Bucket(os.getenv("bucket_name"))
            names_buckets = []

            for buckets in response.objects.all():
                names_buckets.append(buckets.key)

            if name in names_buckets:
                file = request.FILES.get("img")
                print(f"The file is {file}")
            elif name not in names_buckets:
                client.put_object(Bucket=os.getenv("bucket_name"), Key=f"{name}/")
            return HttpResponse("TEST")

        except Exception as error:
            return HttpResponse(f"Error: {error}")
