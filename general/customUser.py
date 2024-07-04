from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is None:
            return False
        return request.user == obj

    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_superuser:
            return form
        form.base_fields['groups'].disabled = True
        form.base_fields['user_permissions'].disabled = True
        form.base_fields['is_staff'].disabled = True
        form.base_fields['is_active'].disabled = True
        form.base_fields['is_superuser'].disabled = True
        form.base_fields['date_joined'].disabled = True
        form.base_fields['last_login'].disabled = True
        
        return form