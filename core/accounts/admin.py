from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name','email')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('full_name','email','password')}),
        ('Personal Info',{'fields':('gender','birth_year','weight','height')}),
        ('Permissions',{'fields':('is_active','is_admin',)}),
    )
    add_fieldsets = (
        (None,{'fields':('full_name','email','password1','password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
