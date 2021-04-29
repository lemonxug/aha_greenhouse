from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import serial_com3

from apps.datas.models import GroundData,AirData
from django.http.response import JsonResponse,HttpResponse

import csv
from datetime import date, datetime
from django.db.models import Q


# Create your views here.

#/datas/nature
# todo：接收数据，保存到数据库中，然后从数据库中取出来
# 温度79.6度湿度21.6%         0
class NatureView(LoginRequiredMixin,View):
    '''环境监测'''
    def get(self,request):

        # 默认显示土壤的各种数据

        # # seri = serial_com3.data.get_data()
        # seri = '温度79.6度湿度21.6%'
        # shidu = seri[2:6]
        # wendu = seri[9:13]
        # place = '大棚一'
        # depth = 20
        # try:
        #     GroundData.objects.create(tu_place=place,tu_depth=depth,tu_shidu=shidu,tu_wendu=wendu)
        # except GroundData.DoesNotExist:
        #     return JsonResponse({'res':'1','errmsg':'数据存储出错'})
        # print('土壤数据存储成功')
        data = GroundData.objects.last()  # 得到最新的数据
        shidu = data.tu_shidu
        wendu = data.tu_wendu
        params = {
            'shidu':shidu,
            'wendu':wendu,
        }
        return render(request,'nature_scan.html',params)

    def post(self,request):

        # 用户点击选择土壤深度和位置后

        seri = serial_com3.get_data()
        print(seri)
        # seri = '温度79.6度湿度21.6%'
        shidu = seri[2:6]
        wendu = seri[9:13]
        place = request.POST.get('place')
        depth = request.POST.get('depth')
        # place = '大棚一'
        # depth = 20
        try:
            GroundData.objects.create(tu_place=place,tu_depth=depth,tu_shidu=shidu,tu_wendu=wendu)
        except GroundData.DoesNotExist:
            return JsonResponse({'res':'1','errmsg':'数据存储出错'})
        print('土壤数据存储成功')
        return JsonResponse({'err':'得到数据','place':place,'depth':depth,'shidu':shidu,'wendu':wendu})




# /datas/data_receive
class Data_Receive(View):
    '''主要负责接收数据，然后给下端发送数据'''
    def post(self, request):
        wendu = request.POST.get('wendu')
        shidu = request.POST.get('shidu')
        oxgen = request.POST.get('oxgen')
        shui = request.POST.get('shui')
        print(wendu+'\n'+shidu+'\n'+oxgen+'\n'+shui)
        try:
            #土壤数据和空气数据同时存储
            #GroundData.objects.create(tu_place=place, tu_depth=depth, tu_shidu=shidu, tu_wendu=wendu)
            AirData.objects.create(is_delete=0,Air_shidu=shidu,Air_wendu=wendu)
        except AirData.DoesNotExist:
            return JsonResponse({'res':'1','errmsg':'数据存储出错'})
        print('空气数据存储成功')
        code = 'off'
        return JsonResponse({'code': code})


# /datas/history
class HistoryView(LoginRequiredMixin,View):
    '''历史数据'''
    def get(self,request):

        return render(request,'historydata.html')



    def post(self,request):
        # 画图
        place = request.POST.get('place')
        depth = request.POST.get('depth')
        try:
            ground_datas = GroundData.objects.filter(tu_depth=depth,tu_place=place)
            air_datas = AirData.objects.filter(is_delete=0)
        except GroundData.DoesNotExist:
            return JsonResponse({'err':'出错了'})
        length = ground_datas.count()
        ground_result = ground_datas[length-27:length]
        length = air_datas.count()
        air_result = air_datas[length - 27:length:1]
        print(type(air_result))
        ground_time_list=[]
        ground_shidu_list = []
        air_time_list = []
        air_wendu_list = []
        air_shidu_list = []
        for res in ground_result:            # "%Y-%m-%d %H:%M:%S"时间格式化
            ground_time_list.append(res.create_time.strftime("%H:%M:%S"))
            ground_shidu_list.append(res.tu_shidu)
        for res in air_result:            # "%Y-%m-%d %H:%M:%S"时间格式化
            air_time_list.append(res.create_time.strftime("%H:%M:%S"))
            air_wendu_list.append(res.Air_wendu)
            air_shidu_list.append(res.Air_shidu)
        return JsonResponse({'ground_shidu_list':ground_shidu_list,'ground_time_list':ground_time_list,
                             'air_time_list':air_time_list,'air_wendu_list':air_wendu_list,'air_shidu_list':air_shidu_list})



class To_Excel(View):
    '''导出数据'''
    def post(self,request):
        # 导出数据
        place1 = request.POST.get('place1')
        depth1 = request.POST.get('depth1')
        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        print(stop_time)

        year1 = int(start_time[0:4])
        month1 = int(start_time[5:7])
        day1 = int(start_time[8:10])
        hour = int(00)
        minute = int(00)
        second = int(00)

        year2 = int(stop_time[0:4])
        month2 = int(stop_time[5:7])
        day2 = int(stop_time[8:10])
        Q(create_time__gt=datetime(year1, month1, day1, hour, minute, second))&Q(create_time__lt=datetime(year2, month2, day2, hour, minute, second))
        start_time = datetime(year1, month1, day1, hour, minute, second)
        stop_time = datetime(year2, month2, day2, hour, minute, second)
        data_daochu = GroundData.objects.filter(Q(create_time__gt=start_time) & Q(create_time__lt=stop_time),tu_place=place1,tu_depth=depth1)
        context = HttpResponse(content_type='text/csv')
        context['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(context)
        writer.writerow(['时间','温度','湿度'])
        for data in data_daochu:
            writer.writerow([data.create_time,data.tu_wendu, data.tu_shidu])
        # return response
        print(context)
        return context

