from django.shortcuts import render
"""Views."""
#from django.views.generic import TemplateView
#from telnetlib import STATUS
#from urllib import request
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Post
from .forms import PostForm, User


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


class PostsView(PermissionRequiredMixin, ListView):
    permission_required = 'core.posts'
    queryset = Post.objects.all()
    template_name = 'core/posts.html' 
    # p = Post.objects.first()
    # post_likes = p.like_set.all()
    
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

class PostsDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'core/post_ob.html'
    pk_url_kwarg = 'id'
    

class PostsDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'core/post_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("posts:list")

class PostsUpdateView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'core/post_update.html'
    pk_url_kwarg = 'id'
    fields = ["title", "content"]
    success_url = reverse_lazy("posts:list")

    

class PostsCreateView(CreateView):
    queryset = Post.objects.all()
    template_name = 'core/post_create.html'
    #fields = ["created_at", "title", "content", "user"]
    success_url = reverse_lazy("posts:list")
    form_class = PostForm

    def form_valid(self, form):
        user = User.objects.first()
        form.instance.user = user
        return super().form_valid(form)

