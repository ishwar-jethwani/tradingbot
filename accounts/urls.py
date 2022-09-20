from django.urls import path,include
from dj_rest_auth.views import LogoutView
from .views import *

urlpatterns = [
    path("register/",include('dj_rest_auth.registration.urls')),
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("auth/",include("allauth.urls")),
    path("verify/",EmailVerification.as_view(),name="verification"),
    path("reset_password/",ResetPassword.as_view(),name="reset_password"),

]