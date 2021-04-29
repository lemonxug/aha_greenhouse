
from apps.user.views import RegisterView,LoginView,IndexView,LogoutView,UserinfoView,PasswordView
from django.urls import path,re_path

urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('index',IndexView.as_view(),name='index'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('userinfo',UserinfoView.as_view(),name='userinfo'),
    path('password',PasswordView.as_view(),name='password'),




]
