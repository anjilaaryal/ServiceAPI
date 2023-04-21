from rest_framework import serializers


class UserSignUpRequest(serializers.Serializer):
    email = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)
    name = serializers.CharField(max_length = 100)
    contact_number =  serializers.CharField(max_length = 100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


  