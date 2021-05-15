from django.contrib import admin
from .models import DeviceControl, DeviceOrder, ThresholdControl, TimerControl, BookControl
# Register your models here.

@admin.register(DeviceControl)
class DeviceControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'status', 'control_type', 'control_id')

@admin.register(DeviceOrder)
class DeviceOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device', 'path', 'parameter')

@admin.register(ThresholdControl)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'indicator', 'threshold', 'order')

@admin.register(TimerControl)
class EnvironmentIndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_time', 'stop_time', 'order', 'repeat_type')

@admin.register(BookControl)
class BookControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_time', 'stop_time', 'order')
