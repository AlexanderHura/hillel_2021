# accounts/forms.py
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
        
class CustomUserCreationForm(UserCreationForm):
    # groups = forms.ModelChoiceField(queryset=Group.objects.all())
    groups = forms.ModelChoiceField(queryset=Group.objects.exclude(name='Администратор'))

    class Meta:
        model = CustomUser
        # fields = "__all__"    
        fields = ('username', 'fio', 'email', 'gender', 'birth_date', 'phone', 'groups')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'fio', 'email', 'gender', 'birth_date', 'phone', 'groups')