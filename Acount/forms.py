from django import forms
from .models import User



class ProfileInfoForm(forms.ModelForm):

    class Meta:
        model=User
        fields=("username","email","first_name","last_name","addres","nation_code","image","phone_number")


class ChangePassworsForm(forms.Form):

    old_password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"password-input"}))
    new_password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"password-input"}))
    new_password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"password-input"}))