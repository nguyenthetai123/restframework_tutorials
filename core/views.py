from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets,generics,status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .permission import MyPermission
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    filter_backends = [SearchFilter]
    # search_fields=['city'] http://127.0.0.1:8000/core/core/?search=asdsad
    # search_fields = ['city', 'name']
    search_fields = ['^city', ]
    pass
class StudentView1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    filter_backends = [OrderingFilter]

    pass
#de custom permision
#has_permission(self,request,view)
#has_object_permission(self,request,view,obj)