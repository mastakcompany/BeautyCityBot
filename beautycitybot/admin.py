from django.contrib import admin

from .models import Clients, Master, Salon, Schedule, Service


class ClientsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'telegram_id', 'username', 'first_name', 'last_name',
        'is_admin',
    ]
    search_fields = ['telegram_id', 'username', 'last_name']


class SalonAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'address', 'time_open', 'time_close'
    ]
    search_fields = ['name', 'address']


class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'salon', 'price'
    ]
    search_fields = ['name', 'price']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['date', 'time_visit', 'salon', 'master', 'service']
    search_fields = ['date', 'salon', 'master']


class MasterAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'salon']
    search_fields = ['full_name', 'salon', 'services']


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Master, MasterAdmin)
