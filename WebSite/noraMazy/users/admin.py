from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Image


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'last_login', 'phone', 'adress1', 'adress2')}),
        ('Infos Personnelles', {'fields': (
            'story',
            'historique',
            'soins',
            'fidelity',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('is_staff', 'email', 'name', 'forename', 'adress1', 'adress2', 'dateNaiss', 'last_login')
    list_filter = ('is_superuser', 'forename')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


class ImageInline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image, PostAdmin)
admin.site.register(User, UserAdmin)
