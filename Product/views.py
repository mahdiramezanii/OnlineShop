import requests
from django.shortcuts import render,redirect
from .models import Product, question
from django.views.generic import DetailView,CreateView

class DetailProductView(DetailView):
    template_name = "Product/detail_product.html"
    model = Product

    def post(self,request,pk):
        product=Product.objects.get(id=pk)
        body=request.POST.get("qa")
        question.objects.create(user=self.request.user,product=product,body=body,parent_id=1)
        return redirect("/")