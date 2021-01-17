from rest_framework import generics, viewsets, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UserBlogPostApiView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.filter(user_id=self.kwargs['user_id'])


class MyBlogPostApiView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        print(1234)
        print(self.request.content_type)
        return BlogPost.objects.filter(user=self.request.user)


class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_queryset(self):
        print((self.request._request))
        qs = BlogPost.objects.all()
        query = self.request.query_params.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)
            ).distinct()
        return qs
