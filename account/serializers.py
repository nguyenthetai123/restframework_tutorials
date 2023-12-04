from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, max_length=30)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = CustomUser.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        # Token.objects.create(user=user)

        return user


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name="post_detail", queryset=CustomUser.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "posts"]
