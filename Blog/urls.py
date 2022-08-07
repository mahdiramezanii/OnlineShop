from django.urls import path
from . import views

app_name="Blog"
urlpatterns=[

    path("",views.BlogView.as_view(),name="blog"),
    path("detail/<int:pk>/",views.DetaillView.as_view(),name="detail")

]