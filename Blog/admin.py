
from django.contrib import admin
from . import models



admin.site.register(models.CategoryBlog)
admin.site.register(models.Article)
admin.site.register(models.Comment)
