from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Employee, Post
from .serializers import EmployeeSerializer, PostSerializer
from rest_framework import status,generics


def employeeListView(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(http_method_names=['GET', 'POST'])
def homepage(request: HttpRequest):
    if request.method == 'POST':
        data = request.data
        response = {'mess': 'dasd', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    res = {'mess': 'dsdsf'}
    return JsonResponse(data=res, status=status.HTTP_200_OK)


class PostListCreateView(APIView):
    serializer_class = PostSerializer

    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        pass


# @api_view(http_method_names=['GET', 'POST'])
# def lists_post(request: HttpRequest):
#     posts = Post.objects.all()
#     if request.method=="POST":
#         data= request.data
#         serializer= PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {'mess': 'dasd', 'data': data}
#             return Response(data=response,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
#     sersializer= PostSerializer(posts,many=True)
#     return Response(sersializer.data, status=status.HTTP_200_OK)

class PostDetail(APIView):
    # cach1
    # def get_object(self, pk):
    #     try:
    #         return Post.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    serializer_class = PostSerializer

    def get(self, request, pk: int):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(instance=post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk:int):
        post=get_object_or_404(Post,pk=pk)
        data=request.data
        serializer= self.serializer_class(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# cach 2
# @api_view(http_method_names=['GET'])
# def post_detail(request: HttpRequest, id: int):
#     post = get_object_or_404(Post, pk=id)
#     serializer = PostSerializer(instance=post)
#     res = {
#         "mess": "post",
#         "data": serializer.data
#     }
#     return Response(data=res, status=status.HTTP_200_OK)

# @api_view(http_method_names=['PUT'])
# def update_post(request: HttpRequest, id: int):
#     post = get_object_or_404(Post, pk=id)
#     if post:
#         data = request.data
#         serializer = PostSerializer(instance=post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {
#                 "mess": "post",
#                 "data": serializer.data
#             }
#             return Response(data=res, status=status.HTTP_200_OK)
#         return Response(data={"error": "not found"}, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['DELETE'])
# def delete_post(request: HttpRequest, id: int):
#     post = get_object_or_404(Post, pk=id)
#     if post:
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response(status=status.HTTP_400_BAD_REQUEST)


class PostList_two(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #xem lai