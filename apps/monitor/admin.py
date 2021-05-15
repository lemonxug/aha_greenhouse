from django.contrib import admin
from .models import GreenHouse, DeviceCategory, Device, EnvironmentIndicator, EnvironmentData

# Register your models here.
@admin.register(GreenHouse)
class GreenHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(DeviceCategory)
class DeviceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Device)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'category', 'greenhouse', 'is_active')

@admin.register(EnvironmentIndicator)
class EnvironmentIndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(EnvironmentData)
class EnvironmentDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'indicator', 'value', 'device', 'create_time')
