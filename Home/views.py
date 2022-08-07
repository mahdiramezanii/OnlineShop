from django.shortcuts import render
from django.views.generic import TemplateView,ListView


class Home(TemplateView):
    template_name = "Home/Home.html"

