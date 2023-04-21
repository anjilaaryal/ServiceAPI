from django.db import models 


class PetTrainer(models.Model):
    name = models.CharField(max_length=100, null=False)
    # contact_number = models.IntegerField()
    description = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)