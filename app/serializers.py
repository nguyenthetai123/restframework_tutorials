from rest_framework import serializers
from .models import Employee,Post


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=155)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)

class PostSerializer(serializers.ModelSerializer):
    title= serializers.CharField(max_length=50)
    class Meta:
        model= Post
        fields= '__all__'