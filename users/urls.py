# urls.py
"""Users app."""

from django.urls import path, include
from .views import UsersView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
