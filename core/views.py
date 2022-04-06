# from django.shortcuts import render
"""Views."""
#from django.views.generic import TemplateView
from telnetlib import STATUS
from django.views.generic import ListView, DetailView

from .models import Post, Like

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
    # p = Post.objects.first()
    # post_likes = p.like_set.all()
    queryset = Post.objects.all()
    # contex_object_name = "posts"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        results = [
            (
            p,
            p.like_set.filter(status=True).count(),
            p.like_set.filter(status=False).count(),            
            )
            for p in posts
        ]
        ctx["results"] = results
        return ctx

class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'core/post_ob.html'
    # pk_url_kwarg = 'id'

class PostDeleteView():
    pass

class PostUpdateView():
    pass
     
class PostCreateView():
    pass



    