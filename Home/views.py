from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from Product.models import Product

class Home(ListView):
    template_name = "Home/Home.html"
    model = Product
