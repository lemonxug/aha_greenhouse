from django.shortcuts import render, redirect, reverse
from apps.controller.models import Device, DeviceControl, DeviceOrder, ControlHistory, ThresholdControl, TimerControl, BookControl
from django.http import HttpResponse, JsonResponse
from datetime import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def change_status(request):
    if request.POST:
        try:
            device_id = request.POST.get('device_id')
            order = request.POST.get('order')
            type_id = request.POST.get('type_id')
            order_id = DeviceOrder.objects.filter(device_id=device_id, name=order).last().id
            flag = control_simulator(device_id, order, order_id, type_id)
            if flag:
                device = DeviceControl.objects.get(device_id=device_id)
                device.status = order
                device.save()
                return JsonResponse({'status': '1'}, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'status': '0'}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'status': '0'}, json_dumps_params={'ensure_ascii': False})


def control_simulator(device_id, order, order_id, control_type):
    try:
        print('{}设备{}中'.format(order, Device.objects.get(id=device_id).name))
        history = ControlHistory(device_id=device_id, order_id=order_id, control_type=control_type)
        history.save()
        print('增加了控制记录')
        return 1
    except:
        return


from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def device_control(request):
    if request.user.is_authenticated:
        devices = DeviceControl.objects.all()
        # todo:动态获取设备前十条操作记录
        history = ControlHistory.objects.all()[:10]
        control_dict = {
            1: '手动',
            2: '阈值',
            3: '定时',
            4: '预约',
        }
        return render(request, 'controller/device_control.html', locals())
    else:
        return redirect(reverse('user:login'))


def create_plan(request):
    if request.POST:
        device_id = request.POST.get('device_id')
        controltype = int(request.POST.get('controltype'))
        threshold_name = request.POST.get('threshold-name')
        indicator = request.POST.get('indicator')
        threshold = request.POST.get('threshold')
        book_name = request.POST.get('book-name')
        book_start = datetime.strptime(request.POST.get('book-start'), '%Y/%m/%d %H:%M:%S')
        book_stop = datetime.strptime(request.POST.get('book-stop'), '%Y/%m/%d %H:%M:%S')
        timer_name = request.POST.get('timer-name')
        timer_start = datetime.strptime(request.POST.get('timer-start'), '%Y/%m/%d %H:%M:%S')
        timer_stop = datetime.strptime(request.POST.get('timer-stop'), '%Y/%m/%d %H:%M:%S')
        timer_repeat = request.POST.get('timer-repeat')
        print(threshold_name, book_name, controltype)
        # try:
        p1 = ThresholdControl(name=threshold_name, device_id=device_id, indicator_id=indicator, threshold=threshold)
        p2 = BookControl(name=book_name, device_id=device_id, start_time=book_start, stop_time=book_stop)
        p3 = TimerControl(name=timer_name, device_id=device_id, start_time=timer_start, stop_time=timer_stop, repeat_type=timer_repeat)
        p1.save()
        p2.save()
        p3.save()
        d = DeviceControl.objects.get(device_id=device_id)
        d.control_type = controltype
        d.save()
        return redirect(reverse('control:device_control'))
        # except Exception as e:
        #     return redirect(reverse('control:device_control'))


def control_history(request):
    pass


def control_plan(request):
    pass
