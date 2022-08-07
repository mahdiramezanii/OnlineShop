from django.urls import path
from . import views

app_name="Acount"
urlpatterns=[
    path("register",views.register_user,name="register"),
    path("login",views.login_user,name="login"),
    path("logout",views.logout_user,name="logout"),
    path("welcome",views.WelcomeView.as_view(),name="welcome"),
    path("profileinfo",views.ProfileInfoView,name="profile_info"),
    path("profile",views.ProfileView.as_view(),name="profile"),
    path("profileorder",views.ProfileOrderView.as_view(),name="profile_order"),
    path("profilefavorate",views.ProfileFavoratesView.as_view(),name="profile_favorate"),
    path("profileaddres",views.ProfileAddresView.as_view(),name="profile_addres"),
    path("profileaddresedit",views.ProfileAddresEditView.as_view(),name="profile_addres_edit"),
    path("profilecomment",views.ProfileCommentView.as_view(),name="profile_comment"),

]