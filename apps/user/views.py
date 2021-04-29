from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views.generic import View
# Create your views here.
from apps.user.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #　登录权限验证
from django.contrib.auth.hashers import make_password  # 修改密码加密



class RegisterView(View):
    '''注册'''
    def get(self,request):
        return render(request,'register.html')


    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print('user_name'+user_name)

        email = request.POST.get('email')
        if  not all([user_name,password,email]):
            return render(request,'register.html',{'errmsg':'数据不完整'})
        try:
            user =User.objects.get(username=user_name)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request,'register.html',{'errmsg':'用户已存在'})
        user = User.objects.create_user(user_name,email,password)
        user.is_active = 1
        user.save()
        # return HttpResponse('ok')
        return redirect(reverse('user:login'))# 反向解析


class LoginView(View):
    '''登录'''
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username,password]):
            return render(request,'login.html',{'errmsg':'数据不完整'})
        # 校验数据
        user = authenticate(username=username, password=password)
        print(username,password)
        print('*'*10)
        print(user)
        if user is not None:
            login(request,user)
            next_url = request.GET.get('next',reverse('news:luntan'))
            response = redirect(next_url)
            print(next_url)
            return response
        else:
            return render(request,'login.html',{'errmsg':'用户名或密码错误'})

# user/logout
class LogoutView(View):
    def get(self,request):
        '''退出登录'''
        logout(request)
        return redirect(reverse('news:luntan'))


class IndexView(LoginRequiredMixin,View):
    '''显示主页'''
    def get(self,request):
        user = request.user
        print(user)
        return render(request,'index.html',{'user':user})


# /user/userinfo
class UserinfoView(LoginRequiredMixin,View):
    '''用户个人中心'''
    def get(self,request):
        user = request.user
        info = User.objects.get(username=user.username)
        address = info.address
        phone = info.phone
        return render(request,'user_information.html',{'address':address,'phone':phone})


    def post(self,request):
        # 处理post提交的数据
        user = request.user
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        user.phone = phone
        user.address = address
        user.save()
        return render(request,'user_information.html',{'address':address,'phone':phone})


class PasswordView(LoginRequiredMixin,View):
    '''密码修改'''
    def get(self,request):
        return render(request,'password_change.html')

    def post(self,request):
        pwd = request.POST.get('pwd')
        user = request.user
        user.password=make_password(pwd)
        user.save()
        return render(request, 'password_change.html')