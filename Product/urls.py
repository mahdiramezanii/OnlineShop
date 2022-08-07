from django.urls import path
from . import views

app_name="Product"

urlpatterns=[
    path("detail/<int:pk>",views.DetailProductView.as_view(),name="detail"),

]