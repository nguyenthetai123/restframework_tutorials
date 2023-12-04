from rest_framework import serializers
from .models import Teach


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teach
        fields='__all__'