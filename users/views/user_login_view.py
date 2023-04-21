from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserLoginRequest
from rest_framework.authtoken.models import Token


class UserLoginView(APIView):

    def post(self, request):
        req_data = request.data
        request_data = UserLoginRequest(data= req_data)
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        email = req_data["email"]
        password = req_data["password"]
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            user_instance = user_qs[0]
            if user_instance.otp_verify:
                password_check = user_instance.check_password(password)
                if password_check:
                    token, created = Token.objects.get_or_create(user = user_instance)
                    print(token)
                    return Response({"key" : token.key}, status = 200)
                else:
                    return Response({"msg" : "Invalid password"}, status = 400)
            else:
                return Response({"msg" : "User not activated"}, status = 400)
        else:
            return Response({"msg" : "Invalid email"}, status = 400)