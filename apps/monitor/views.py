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
    if request.user.is_authenticated:
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
    else:
        return redirect(reverse('user:login'))


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
    if request.user.is_authenticated:
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
    else:
        return redirect(reverse('user:login'))

def analysis(request):
    def check(arg, defaut):
        if arg:
            return arg
        return defaut
    if request.user.is_authenticated:
        if request.POST:
            gshidu_device = check(request.POST.get('gshidu_device'), 7)
            gwendu_device = check(request.POST.get('gwendu_device'), 31)
            ashidu_device = check(request.POST.get('ashidu_device'), 1)
            awendu_device = check(request.POST.get('awendu_device'), 3)
            try:
                ground_wendu = EnvironmentData.objects.filter(indicator_id=5, device_id=gwendu_device)
                ground_shidu = EnvironmentData.objects.filter(indicator_id=6, device_id=gshidu_device)
                air_shidu = EnvironmentData.objects.filter(indicator_id=2, device_id=ashidu_device)
                air_wendu = EnvironmentData.objects.filter(indicator_id=1, device_id=awendu_device)
            except EnvironmentData.DoesNotExist:
                return JsonResponse({'err':'出错了'})
            ground_wendu_time = [i.create_time.strftime("%H:%M:%S") for i in ground_wendu[:27]]
            ground_wendu_data = [i.value for i in ground_wendu[:22]]
            ground_shidu_time = [i.create_time.strftime("%H:%M:%S") for i in ground_shidu[:27]]
            ground_shidu_data = [i.value for i in ground_shidu[:22]]
            air_wendu_time = [i.create_time.strftime("%H:%M:%S") for i in air_wendu[:27]]
            air_wendu_data = [i.value for i in air_wendu[:22]]
            air_shidu_time = [i.create_time.strftime("%H:%M:%S") for i in air_shidu[:27]]
            air_shidu_data = [i.value for i in air_shidu[:22]]
            return JsonResponse({'ground_wendu_time': ground_wendu_time, 'ground_wendu_data': ground_wendu_data,
                                 'ground_shidu_time': ground_shidu_time, 'ground_shidu_data': ground_shidu_data,
                                 'air_wendu_time':air_wendu_time, 'air_wendu_data':air_wendu_data,
                                 'air_shidu_time':air_shidu_time, 'air_shidu_data':air_shidu_data,
                                 })
        ashidu_device = Device.objects.filter(id__in= EnvironmentData.objects.filter(indicator_id=2).values('device_id').distinct())
        awendu_device = Device.objects.filter(id__in= EnvironmentData.objects.filter(indicator_id=1).values('device_id').distinct())
        gshidu_device = Device.objects.filter(id__in= EnvironmentData.objects.filter(indicator_id=6).values('device_id').distinct())
        gwendu_device = Device.objects.filter(id__in= EnvironmentData.objects.filter(indicator_id=5).values('device_id').distinct())
        return render(request, 'monitor/analysis.html', locals())
    else:
        return redirect(reverse('user:login'))