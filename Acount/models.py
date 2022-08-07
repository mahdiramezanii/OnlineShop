from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nation_code=models.CharField(max_length=15,null=True,blank=True)
    addres=models.TextField(help_text="آدرس خود را وارد کنید",null=True,blank=True)
    image=models.FileField(null=True,blank=True,upload_to="User/image")
    phone_number=models.CharField(max_length=15,null=True,blank=True)


