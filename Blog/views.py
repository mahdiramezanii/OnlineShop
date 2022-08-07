from django.shortcuts import render, redirect
from .models import Article, CategoryBlog
from django.views.generic import TemplateView, ListView,DetailView
from .models import Article,Comment

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


    def post(self,request,pk):
        name=request.POST.get("name")
        titel=request.POST.get("titel")
        text=request.POST.get("text")
        parent_id=request.POST.get("parent_id")
        print(parent_id)
        if name and titel and text:
            Comment.objects.create(user=request.user,article_id=pk,titel=titel,body=text,parent_id=parent_id)

        return redirect("/")




