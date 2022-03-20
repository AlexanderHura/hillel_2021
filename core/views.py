# from django.shortcuts import render
"""Views."""
#from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Post

# def posts(requests):
#     posts = Post.objects.all()
#     results = ", ".join([post.title for post in posts])
# 
#     # posts = "post 1 : King Artur"
#     return HttpResponse(f"<h1>{results}</h1>")


# class PostsView(TemplateView):
#     template_name = 'core/posts.html'   
# 
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all()
#         return ctx


class PostsView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()