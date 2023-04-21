from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from services.models import BabySitter
from services.serializers import BabySitterRequest
from booking_service.models import Reservation
from booking_service.serializers import ReservationRequest
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta


class ReserveBabySitterView(APIView):

    def post(self,request):
        user = request.user
        req_data = request.data
        request_data = ReservationRequest(data=req_data)
        _ = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data

        time = req_data["service_time"]
        
 
            # return Response({"msg" : "Babysitter Booked"}, status = 200)

            # return Response({"msg" : "Invalid Babysitter"}, status = 400)



