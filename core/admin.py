# Modules of admin panel
"""Django admin panel."""
from django.contrib import admin
from .models import Like, Post


class LikeTabularInLine(admin.TabularInline):
    """LikeTabularInLine."""

    model = Like


class PostAdmin(admin.ModelAdmin):
    """PostAdmin class."""

    inlines = [LikeTabularInLine]

    class Meta:
        """Meta class."""

        model = Post


admin.site.register(Post, PostAdmin)
