from rest_framework import serializers


class ReservationRequest(serializers.Serializer):
    service_name = serializers.CharField(max_length = 100)
    service_time = serializers.CharField(max_length = 100)