from rest_framework import serializers


class UserLoginRequest(serializers.Serializer):
    password = serializers.CharField(max_length = 100)
    email = serializers.CharField(max_length = 100)