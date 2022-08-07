from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from .forms import ProfileInfoForm


def login_user(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("Home:Home")


    return render(request,"Acount/login.html")


def register_user(request):

    context={
        "errors":[],
    }

    if request.method=="POST":
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if username and password1 and password2:
            if User.objects.filter(username=username).exists():
                context["errors"].append("نام کاربری تکراری است")

            elif password1 != password2:
                context["errors"].append("رمز ها شباهت ندارد")

            else:
                user=User.objects.create(username=username,password=password1)
                user.set_password(password1)
                user.save()
                login(request,user)
                return redirect("Acount:welcome")

    return render(request,"Acount/register.html",context)


def logout_user(request):

    logout(request)

    return redirect("Home:Home")

class WelcomeView(TemplateView):
    template_name = "Acount/welcome.html"


def ProfileInfoView(request):
    user=request.user
    form=ProfileInfoForm(instance=user)

    if request.method=="POST":
        form=ProfileInfoForm(instance=user,data=request.POST)

        if form.is_valid():
            form.save()
    else:
        form=ProfileInfoForm(instance=user)
    return render(request,"Acount/profile_personal.html",{"form":form})


class ProfileView(TemplateView):
    template_name = "Acount/profile.html"

class ProfileOrderView(TemplateView):
    template_name = "Acount/profile_order.html"

class ProfileFavoratesView(TemplateView):
    template_name = "Acount/profile_favorites.html"

class ProfileAddresView(TemplateView):
    template_name = "Acount/profile_address.html"

class ProfileAddresEditView(TemplateView):
    template_name = "Acount/profile_addres_edit.html"

class ProfileCommentView(TemplateView):
    template_name = "Acount/profile_comment.html"

