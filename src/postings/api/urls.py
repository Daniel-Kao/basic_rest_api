from django.urls import path
from .views import BlogPostRudView, BlogPostApiView, MyBlogPostApiView

urlpatterns = [
    path('<int:pk>/', BlogPostRudView.as_view(), name="post-rud"),
    path('me/', MyBlogPostApiView.as_view(), name="my-post-list"),
    path('', BlogPostApiView.as_view(), name="post-list"),
]
