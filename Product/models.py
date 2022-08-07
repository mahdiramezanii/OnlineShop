from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class galery_image(models.Model):
    image=models.ImageField(upload_to="product/image")
    created=models.DateTimeField(auto_now_add=True)

class category(models.Model):
    titel=models.CharField(max_length=150)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

class information(models.Model):
    item=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item



class Product(models.Model):
    titel=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product/image",blank=True,null=True)
    image_galery=models.ManyToManyField(galery_image)
    price=models.IntegerField()
    offprice=models.IntegerField(null=True,blank=True,default=None)
    description=models.TextField()
    category=models.ManyToManyField(category)
    slug=models.SlugField(null=True,blank=True)
    information=models.ManyToManyField(information)
    created=models.DateTimeField(auto_now_add=True)

    def get_absolut_url(self):

        return reverse("Product:detail",kwargs={"pk":self.id})

    def save(self,*args,**kwargs):
        self.slug=slugify(self.titel)

        super(Product, self).save(*args,*kwargs)

    def __str__(self):

        return self.titel

class question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="question")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="question")
    created=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replay")



    def __str__(self):

        return self.body[:20]







