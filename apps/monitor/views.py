from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from apps.monitor.models import GreenHouse, DeviceCategory, Device, EnvironmentIndicator, EnvironmentData
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

# Create your views here.
def global_variable(request):
    house_list = GreenHouse.objects.all()
    device_category_list = DeviceCategory.objects.all()
    indicator_list = EnvironmentIndicator.objects.all()
    device_list = Device.objects.all()
    return locals()


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_data(request):
    if request.POST:
        try:
            device_id = request.POST.get('device_id')
            indicator_id = request.POST.get('indicator_id')
            value = request.POST.get('value')
            data = EnvironmentData(device_id=device_id, indicator_id=indicator_id, value=value)
            data.save()
            return JsonResponse({'status': '1'}, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'status': '0'}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'status': '0'}, json_dumps_params={'ensure_ascii': False})


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
                'wendu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=1).first(),
                'shidu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=2).first(),
                'co2': EnvironmentData.objects.filter(device__in=house_device, indicator_id=3).first(),
                'shine': EnvironmentData.objects.filter(device__in=house_device, indicator_id=4).first(),
                'twendu': EnvironmentData.objects.filter(device__in=house_device, indicator_id=5).first(),
                'tshuifen': EnvironmentData.objects.filter(device__in=house_device, indicator_id=6).first(),
            }
            data_index.append(data)
        return render(request, 'monitor/index.html', locals())
    else:
        return redirect(reverse('user:login'))


def detail(request, house_id):
    house = get_object_or_404(GreenHouse, id=house_id)
    # device_house = get_list_or_404(Device, greenhouse=house_id)
    device_house = Device.objects.filter(greenhouse=house_id, category=1)
    data_list = []
    for device in device_house:
        # 获取每传感器最新记录的值
        # data_device = device.environmentdata_set.order_by('create_time').last()
        data_device = device.environmentdata_set.first()
        data = {
            'device': device,
            'data': data_device
        }
        data_list.append(data)
    # data_device = EnvironmentData.objects.filter(device__in=device_house)
    return render(request, 'monitor/detail.html', locals())


def get_data(request, house_id):
    house = get_object_or_404(GreenHouse, id=house_id)
    device_house = Device.objects.filter(greenhouse=house_id, category=1)
    data_list = []
    for device in device_house:
        data_device = device.environmentdata_set.last()
        data = {
            'house': house.name,
            'device_name': device.name,
            'device_location': device.location,
            'data_indicator': data_device.indicator.name,
            'data_value': data_device.value,
            'data_create_time': data_device.create_time,
        }
        data_list.append(data)
    return JsonResponse({'data': data_list}, json_dumps_params={'ensure_ascii': False})


def query_environmentdata(request):
    page = request.GET.get('page')
    house = request.GET.get('house')
    device = request.GET.get('device')
    indicator = request.GET.get('indicator')
    time1 = request.GET.get('time1')
    time2 = request.GET.get('time2')

    if time1:
        time1 = datetime.strptime(time1, '%Y-%m-%d')
    if time2:
        time2 = datetime.strptime(time2, '%Y-%m-%d')

    size = 15
    data_list = EnvironmentData.objects.all()
    if not page:
        page = 1
    if house:
        house_device = Device.objects.filter(greenhouse=house, category=1)
        data_list = EnvironmentData.objects.filter(device__in=house_device)
    if device:
        data_list = EnvironmentData.objects.filter(device=device)
    if indicator:
        data_list = EnvironmentData.objects.filter(indicator=indicator)
    if time1:
        if time2:
            data_list = EnvironmentData.objects.filter(create_time__gt=time1, create_time__lt=time2)
        else:
            data_list = EnvironmentData.objects.filter(create_time__gt=time1)
    else:
        if time2:
            data_list = EnvironmentData.objects.filter(create_time__lt=time2)
    paginator = Paginator(data_list, size)
    try:
        data_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        data_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'monitor/environment_data.html', locals())


def analysis(request):
    redirect(reverse('monitor:environment_data'))