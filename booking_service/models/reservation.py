from django.db import models 



TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)

class Reservation(models.Model):
    user = models.ForeignKey("users.User", models.DO_NOTHING)
    service_name = models.CharField(max_length=100)
    service_time = models.CharField(max_length=100, choices=TIME_CHOICES, default="10 AM")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)