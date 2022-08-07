from django.shortcuts import render
from .models import Article, CategoryBlog
from django.views.generic import TemplateView, ListView,DetailView
from .models import Article

from jalali_date import datetime2jalali, date2jalali


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


class BlogView(ListView):
    template_name = "Blog/blog.html"
    model = Article
    paginate_by = 8


class DetaillView(DetailView):
    template_name = "Blog/detail.html"
    model = Article

