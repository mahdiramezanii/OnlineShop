from django.urls import path
from . import views
app_name="Contact_us"
urlpatterns=[
    path("",views.ContactView.as_view(),name="contact_us")
]
