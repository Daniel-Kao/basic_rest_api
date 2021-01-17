from django.urls import path
from .views import BlogPostRudView, BlogPostApiView, MyBlogPostApiView, UserBlogPostApiView

urlpatterns = [
    path('<int:pk>/', BlogPostRudView.as_view(), name="post-rud"),
    path('user/<int:user_id>/', UserBlogPostApiView.as_view(), name="user-post-list"),
    path('me/', MyBlogPostApiView.as_view(), name="my-post-list"),
    path('', BlogPostApiView.as_view(), name="post-list"),
]
