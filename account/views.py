from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import models
from rest_framework import viewsets, status
# Create your models here.
from app.models import Post
from app.serializers import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import SignUpSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]
    # def list(self,request):
    #     queryset= Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    # def retrieve(self,request,pk=None):
    #     post=get_object_or_404(Post,pk=pk)
    #     serializer=PostSerializer(post)
    #     return Response(serializer.data,status=status.HTTP_200_OK)


class SignupView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#BasicAuthetication
#request.user will be django user instance
#request.auth will be None