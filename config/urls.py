from django.contrib import admin
from django.urls import  include, path
from django.views.generic import RedirectView




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path('', RedirectView.as_view(url='/posts/', permanent=True))
]
