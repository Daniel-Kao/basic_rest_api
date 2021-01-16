from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BlogPostApiView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
