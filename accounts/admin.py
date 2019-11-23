from .forms import UserCreationForm
from .models import MyUser
# from accounts.Models.HinhAnhCXModel import Hinhanhcayxanh
from accounts.models import Trangthaitc
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework.authtoken.admin import TokenAdmin

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ('username', 'password', 'email', 'ngaysinh', 'gioitinh', 'diachi', 'is_admin', 'is_active', 'is_staff', 'duongdanavatar')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'gioitinh', 'diachi', 'ngaysinh', 'duongdanavatar')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff')})
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
# admin.site.register(Hinhanhcayxanh)
admin.site.register(Trangthaitc)
admin.site.unregister(Group)



TokenAdmin.raw_id_fields = ['user']