from django.db import models
from apps.monitor.models import Device, EnvironmentIndicator

# Create your models here.


class DeviceControl(models.Model):
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    status = models.CharField('控制状态', max_length=10, default='启动')
    control_type = models.IntegerField('控制方式', default=1)   # 1-手动，2-阈值，3-定时，4-预约
    control_id = models.IntegerField('控制信息', null=True)   # 对应的control表的id

    class Meta:
        verbose_name = '设备控制表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.device.name


class DeviceOrder(models.Model):
    name = models.CharField('指令名称', max_length=100)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    path = models.CharField('路径', max_length=100)
    parameter = models.CharField('参数', max_length=100)

    class Meta:
        verbose_name = '设备指令表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.name


class ThresholdControl(models.Model):
    name = models.CharField('指令名称', max_length=100)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    indicator = models.ForeignKey(EnvironmentIndicator, on_delete=models.DO_NOTHING, verbose_name='环境指标', blank=True, null=True)
    threshold = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='阈值')
    order = models.ForeignKey(DeviceOrder, on_delete=models.DO_NOTHING, verbose_name='设备指令', blank=True, null=True)

    class Meta:
        verbose_name = '阈值控制表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数


class BookControl(models.Model):
    name = models.CharField('指令名称', max_length=100)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    order = models.ForeignKey(DeviceOrder, on_delete=models.DO_NOTHING, verbose_name='设备指令', blank=True, null=True)
    start_time = models.DateTimeField('开始时间')
    stop_time = models.DateTimeField('结束时间')

    class Meta:
        verbose_name = '预约控制表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数


class TimerControl(models.Model):
    name = models.CharField('指令名称', max_length=100)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    order = models.ForeignKey(DeviceOrder, on_delete=models.DO_NOTHING, verbose_name='设备指令', blank=True, null=True)
    start_time = models.DateTimeField('开始时间')
    stop_time = models.DateTimeField('结束时间')
    repeat_type = models.CharField('重复方式', max_length=10, default='不重复')   # 0-不重复，1-每天，2-每2天

    class Meta:
        verbose_name = '定时控制表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数


class ControlHistory(models.Model):
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, verbose_name='设备名称', blank=True, null=True)
    order = models.ForeignKey(DeviceOrder, on_delete=models.DO_NOTHING, verbose_name='设备指令', blank=True, null=True)
    control_type = models.IntegerField('控制方式')
    create_time = models.DateTimeField('操作时间', auto_now_add=True)

    class Meta:
        verbose_name = '设备命令表'  # 可读的名字
        verbose_name_plural = verbose_name  # 可读的名字的复数

    def __str__(self):
        return self.control_type




