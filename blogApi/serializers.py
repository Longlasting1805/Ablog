from rest_framework import serializers
from .models import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content', 'date']
