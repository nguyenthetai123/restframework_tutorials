from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeacherSerializer
from .models import Teach
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

# Create your views here.

@api_view(http_method_names=['GET', 'POST'])
def hello_word(request):
    if request.method == 'GET':
        stu = Teach.objects.all()
        serializer = TeacherSerializer(instance=stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['PUT', 'DELETE'])
def tech_api(requets, pk):
    tech = get_object_or_404(Teach, pk=pk)
    if requets.method == 'PUT':
        if tech:
            data = requets.data
            serializer = TeacherSerializer(tech, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if requets.method == 'DELETE':
        if tech:
            tech.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        pass


class teacherView(APIView):
    def get(self, request):
        tech = Teach.objects.all()
        serializer = TeacherSerializer(tech, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechDetail(APIView):
    def get(self, request, pk):
        tech = get_object_or_404(Teach, pk=pk)
        serializer = TeacherSerializer(tech)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, requets, pk):
        tech = get_object_or_404(Teach, pk=pk)
        serializer = TeacherSerializer(tech, data=requets.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tech = Teach.objects.get(pk=pk)
        tech.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class TechList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teach.objects.all()
    serializer_class = TeacherSerializer

class List(generics.GenericAPIView,mixins.CreateModelMixin):
    queryset = Teach.objects.all()
    serializer_class = TeacherSerializer