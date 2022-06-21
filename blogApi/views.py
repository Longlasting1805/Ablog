from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogSerializer


# Create your views here.

class BlogView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        blog = BlogPost.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)

    def patch(self, request, id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog = self.get_object(id)
        blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
