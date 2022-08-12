# urls.py
"""Users app."""

from django.urls import path, include
from .views import UsersView
from .views import SignUpView, LoginView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path("signup/", SignUpView.as_view(), name="signup"),

]
