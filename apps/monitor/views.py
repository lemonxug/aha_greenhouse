from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from apps.monitor.models import GreenHouse, DeviceCategory, Device, EnvironmentIndicator, EnvironmentData
from django.http import JsonResponse


# Create your views here.
def global_variable(request):
    house_list = GreenHouse.objects.all()
    device_category_list = DeviceCategory.objects.all()
    indicator_list = EnvironmentIndicator.objects.all()
    device_list = Device.objects.all()
    return locals()


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
        data_device = device.environmentdata_set.last()
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


