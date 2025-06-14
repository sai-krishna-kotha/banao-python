from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display fields in the user list page
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'user_type',
        'is_staff',
    )

    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')

    search_fields = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('User Type and Profile', {
            'fields': ('user_type', 'profile_picture'),
        }),
        ('Address Information', {
            'fields': ('address_line1', 'city', 'state', 'pincode'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Type and Profile', {
            'fields': ('user_type', 'profile_picture', 'first_name', 'last_name'),
        }),
        ('Address Information', {
            'fields': ('address_line1', 'city', 'state', 'pincode'),
        }),
    )
