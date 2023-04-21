from django.urls import path, include
from booking_service.views import ReserveBabySitterView

urlpatterns = [
    path('babysitter/', ReserveBabySitterView.as_view()),
]