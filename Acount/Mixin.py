from django.shortcuts import redirect

class LoginRequired:
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
                return redirect("Home:Home")
        return super(LoginRequired, self).dispatch(request,*args,**kwargs)