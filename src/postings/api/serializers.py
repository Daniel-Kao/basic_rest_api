from rest_framework import serializers
from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = BlogPost
        fields = ['pk', 'user', 'user_name', 'title', 'content', 'timestamp']
        read_only_fields = ['user']
        extra_kwargs = {'content': {'write_only': True}}

    # def validate_title(self, value):
    #     qs = BlogPost.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('title must be unique')
    #     return value
