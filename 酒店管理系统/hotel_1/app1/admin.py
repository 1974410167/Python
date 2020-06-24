from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# Register your models here.

from .models import House,Customer

admin.site.site_header = '酒店管理系统'

class HouseAdmin(admin.ModelAdmin):

    ordering = ['house_type']
    # fields = ('house_type','is_check_in','price')
    list_display = ['house_type','is_check_in','price']


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name','phone']

    ordering = ['name']
    # fields = ('name','gender','phone','id_card')
    list_display = ['name','gender','phone','id_card','House_id']


admin.site.register(House,HouseAdmin)
admin.site.register(Customer,CustomerAdmin)


