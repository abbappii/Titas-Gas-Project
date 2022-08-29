from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from AuthenticationApp import models as auth_model


# Register your models here.
# User Authentication Model
@admin.register(auth_model.User)
class AuthUser(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'full_name', 'profile_pic', 'phone_number', 'birthDate', 'gender', 'otp',
        'otp_time', 'is_staff', 'is_active', 'is_superuser', 'is_suspended', 'last_login', 'date_joined')


@admin.register(auth_model.UserPermissionModel)
class UserPermission(admin.ModelAdmin):
    list_display = ('user', 'read', 'create', 'update', 'delete', 'super_access',)
