# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    # list_display = ['username', 'fio', 'email', 'gender', 'birth_date', 'user_groups_display', 'is_staff']
    list_display = ['username', 'fio', 'email', 'gender', 'birth_date', 'phone', 'user_groups_display', 'is_staff']


    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'phone',
                    'groups',
                    
                    
                )
            }
        )
    )

    # Edit user
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'phone',
                )
            }
        )
    )

    def user_groups_display(self, user):
        try:
            groups = []
            for group in user.groups.all():
                groups.append(group.name)
            return ', '.join(groups)
        except:
            return '-'


