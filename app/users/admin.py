from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.db import models



class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'gender', 'category', 'phone', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'full_name', 'phone')
    list_filter = ('is_active', 'is_staff', 'gender', 'category')
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'gender', 'birth_date', 'category', 'phone', 'reitforusers')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Параметры для формы изменения пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'gender', 'birth_date', 'category', 'phone', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    # Настройка отображения и фильтрации по категориям (можно добавить более удобное отображение для категорий и полов)
    list_display_links = ('email', 'full_name')
    
    # Защищенные поля для админки
    readonly_fields = ('last_login', 'date_joined')

    # Сортировка по умолчанию
    ordering = ('email',)

    # Настройки для отображения в форме добавления и изменения
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget},
    }
# Регистрируем кастомную модель пользователя в админке
admin.site.register(User, CustomUserAdmin)
