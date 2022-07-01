from django.urls import path
from .views import PostsView, PostsDetailView, PostsDeleteView, PostsUpdateView, PostsCreateView

app_name = "posts"

urlpatterns = [
    path("posts/", PostsView.as_view(), name = "list"),
    path("post_detail/<int:id>/", PostsDetailView.as_view(), name= "detail"),
    path("post_delete/<int:id>/", PostsDeleteView.as_view(), name="delete"),
    path("post_update/<int:id>/", PostsUpdateView.as_view(), name="update"),
    path("post_create/", PostsCreateView.as_view(), name="create"),
    
] 
