from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from django.utils.translation import gettext_lazy as translate

from .models import Account


class AccountAdmin(BaseUserAdmin):
    """Defile the admin pages for user accounts."""
    ordering = ['id']
    list_display = ['username', 'password']
    fieldsets = (
        ('Account', {'fields': ('username', 'password')}),
        (
            translate('Permissions'),
            {
                'fields': (
                    # optional field
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password',
                # optional fields
                'is_active',
                'is_staff',
                'is_superuser',

            )
        }),
    )


admin.site.register(Account, AccountAdmin)
