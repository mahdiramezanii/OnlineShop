from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "Contact_us/contact_us.html"
