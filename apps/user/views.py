from django.shortcuts import render, redirect, reverse
from apps.user.models import UserAccount
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin    # 登录权限验证
from django.contrib.auth.hashers import make_password    # 修改密码加密
from apps.monitor.models import GreenHouse, EnvironmentData, Device
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # avatar = request.FILES.get("avatar")
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        is_exist = 0 if len(UserAccount.objects.filter(username=username))==0 else 1
        if not is_exist:
            user = UserAccount.objects.create_user(username=username, email=email, phone=phone,
                                            password=password, is_active=1)
            user.save()
            return redirect(reverse('user:login'))    # 反向解析
        else:
            return render(request, 'user/register.html', {'error_message': '注册失败，请重试！'})


def log_in(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('user:index'))    # 反向解析
        else:
            return render(request, 'user/login.html', {'error_message': '用户名或密码错误!'})

# user/logout
def log_out(request):
    logout(request)
    # return redirect(reverse('news:luntan'))
    return redirect(reverse('index'))


def index(request):
    if request.user.is_authenticated:
        indicators = [1, 2, 3, 4, 5, 6]   # 首页展示的指标
        house_list = GreenHouse.objects.all()
        data_index = []
        for house in house_list:
            house_device = Device.objects.filter(greenhouse=house.id)
            data = {
                'id': house.id,
                'name': house.name,
                'wendu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=1).last(),
                'shidu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=2).last(),
                'co2': EnvironmentData.objects.filter(device__in=house_device, indicator_id=3).last(),
                'shine': EnvironmentData.objects.filter(device__in=house_device, indicator_id=4).last(),
                'twendu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=5).last(),
                'tshuifen': EnvironmentData.objects.filter(device__in=house_device, indicator_id=6).last(),
            }
            data_index.append(data)
        return render(request, 'user/index.html', locals())
        # return render(request, 'user/index.html')
    else:
        return redirect(reverse('user:login'))


def userinfo(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'user/user_info.html')
        elif request.method == 'POST':
            user = request.user
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            user.phone = phone
            user.address = address
            user.save()
            return render(request, 'user/user_info.html')
    else:
        return redirect(reverse('user:login'))


def reset_password(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'user/reset_password.html')
        elif request.method == 'POST':
            pwd = request.POST.get('pwd')
            user = request.user
            user.password = make_password(pwd)
            user.save()
            return render(request, 'user/reset_password.html')
    else:
        return redirect(reverse('user:login'))
