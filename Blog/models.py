from django.db import models
from Acount.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class CategoryBlog(models.Model):
    titel=models.CharField(max_length=50)
    crated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

class Article(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name="article")
    category=models.ForeignKey(CategoryBlog,on_delete=models.SET_NULL,null=True)
    titel=models.CharField(max_length=200)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="Blog/img")
    date=models.DateField(default=timezone.now)
    slug=models.SlugField(null=True,blank=True)


    def get_absolut_url(self):

        return reverse("Blog:detail",kwargs={"pk":self.id})

    def save(self,*args,**kwargs):

        self.slug=slugify(self.titel)

        super(Article,self).save(*args,**kwargs)

    def __str__(self):

        return self.titel


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comment")
    created=models.DateField(auto_now_add=True)
    body=models.TextField()
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replay")


    def __str__(self):

        return self.body[:25]