from rest_framework import generics, viewsets, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MyBlogPostApiView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.filter(user=self.request.user)


class BlogPostApiView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
