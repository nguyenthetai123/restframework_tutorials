from django.shortcuts import render

from django.db import models
from rest_framework import viewsets, status
# Create your models here.
from app.models import Post
from app.serializers import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # def list(self,request):
    #     queryset= Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    # def retrieve(self,request,pk=None):
    #     post=get_object_or_404(Post,pk=pk)
    #     serializer=PostSerializer(post)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
