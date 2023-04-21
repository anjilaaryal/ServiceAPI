from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User, OtpUser
from users.serializers import UserSignUpRequest, UserSerializer
from django.db import transaction
import random


class UserSignUpView(APIView):

    @transaction.atomic
    def post(self, request):
        req_data = request.data
        request_data = UserSignUpRequest(data = req_data)
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        user_qs = User.objects.filter(email = req_data["email"])
        if user_qs.exists():
            return Response({"msg" : "Email is already used by another user"}, status=400)
        user_instance = UserSerializer.create(req_data)
        resp = self.generate_response(user_instance)

        otp_val = self.generate_otp()
        OtpUser.objects.create(otp_value = otp_val, user= user_instance)
        return Response(resp, status=200)
    
    def generate_response(self, instance):
        resp = {}
        resp["id"] = instance.id
        resp["email"] = instance.email
        return resp


    def generate_otp(self):
        return random.randint(100000, 999999)