from django.db import models

class OtpUser(models.Model):
    otp_value = models.IntegerField()
    user = models.ForeignKey("users.User", models.DO_NOTHING)