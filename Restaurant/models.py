from django.db import models


# Create your models here.

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    comments = models.TextField(null=True, blank=True)
