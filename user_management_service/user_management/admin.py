from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'full_name')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields': ('role', 'full_name' )}),
    )
    list_display = ['username', 'email', 'full_name', 'role']

admin.site.register(CustomUser,CustomUserAdmin)