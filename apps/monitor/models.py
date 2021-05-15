from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 大棚
class GreenHouse(models.Model):
    name = models.CharField('大棚名称', max_length=100)

    class Meta:
        verbose_name = '大棚列表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.name


# 设备分类
class DeviceCategory(models.Model):
    name = models.CharField('设备分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '设备分类'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.name


# 设备
class Device(models.Model):
    name = models.CharField('名称', max_length=100)
    location = models.CharField('监控点', max_length=100)
    status = models.CharField('设备状态', max_length=100)
    category = models.ForeignKey(DeviceCategory, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    greenhouse = models.ForeignKey(GreenHouse, on_delete=models.DO_NOTHING, verbose_name='大棚', blank=True, null=True)
    is_active = models.BooleanField('是否在用', default=True,)

    class Meta:
        verbose_name = '设备'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.name


# 指标名称
class EnvironmentIndicator(models.Model):
    name = models.CharField('指标名称', max_length=100)

    class Meta:
        verbose_name = '环境指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 环境数据
class EnvironmentData(models.Model):
    indicator = models.ForeignKey(EnvironmentIndicator, on_delete=models.DO_NOTHING, verbose_name='环境指标', blank=True, null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='监测值')
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    create_time = models.DateTimeField('记录时间', auto_now_add=True)


    class Meta:
        verbose_name = '环境数据'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return str(self.indicator) + '-' + str(self.value)

