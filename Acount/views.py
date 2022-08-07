from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.base import View
from .models import User
from  django.contrib.auth import authenticate,login,logout
from .forms import ProfileInfoForm,ChangePassworsForm
from .Mixin import LoginRequired

def login_user(request):
    if request.user.is_authenticated:
        return redirect("Home:Home")

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("Home:Home")


    return render(request,"Acount/login.html")


def register_user(request):
    if request.user.is_authenticated:
        return redirect("Home:Home")
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
    if request.user.is_authenticated:
        return redirect("Home:Home")
    logout(request)

    return redirect("Home:Home")

class WelcomeView(LoginRequired,TemplateView):

    template_name = "Acount/welcome.html"


def ProfileInfoView(request):
    user=request.user
    form=ProfileInfoForm(instance=user)

    if request.method=="POST":
        form=ProfileInfoForm(request.POST,
                             request.FILES,
                             instance=request.user)

        if form.is_valid():
            form.save()

    else:
        form=ProfileInfoForm(instance=user)
    return render(request,"Acount/profile_personal.html",{"form":form})


class ProfileView(LoginRequired,TemplateView):
    template_name = "Acount/profile.html"

class ProfileOrderView(LoginRequired,TemplateView):
    template_name = "Acount/profile_order.html"

class ProfileFavoratesView(LoginRequired,TemplateView):
    template_name = "Acount/profile_favorites.html"

class ProfileAddresView(LoginRequired,TemplateView):
    template_name = "Acount/profile_address.html"

class ProfileAddresEditView(LoginRequired,TemplateView):
    template_name = "Acount/profile_addres_edit.html"

class ProfileCommentView(LoginRequired,TemplateView):
    template_name = "Acount/profile_comment.html"

class ChangPassword(LoginRequired,View):

    def post(self,request,*args,**kwargs):
        errors=[]
        form=ChangePassworsForm(data=request.POST)
        user=request.user
        if form.is_valid():
            old_pass=form.cleaned_data.get("old_password")
            new_pass1=form.cleaned_data.get("new_password1")
            new_pass2=form.cleaned_data.get("new_password2")

            if not user.check_password(old_pass):
                errors.append("پسورد قبلی اشتباه است!")
            elif new_pass1 != new_pass2:
                errors.append("پسورد های جدید شباهت ندارد!")
            else:
                user.set_password(new_pass1)
                user.save()
                return redirect("Acount:profile")

        return render(request,"Acount/password_change.html",{"form":form,"errors":errors})

    def get(self,request,*args,**kwargs):
        form=ChangePassworsForm()
        return render(request,"Acount/password_change.html",{"form":form})
