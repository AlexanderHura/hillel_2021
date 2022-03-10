from django.contrib import admin

from .models import Like, Post
#@admin.register(Like) 
class LikeTabularInLine(admin.TabularInline):
        model = Like


#@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInLine]
    class Meta:
        model = Post
    
admin.site.register(Post, PostAdmin)

#admin.site.register(Like)

