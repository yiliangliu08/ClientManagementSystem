from django.db import models
from django.contrib.auth.models import User
import uuid


class Client(models.Model):
    client_id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)


class Package(models.Model):
    card_Id = models.UUIDField()
    client_id = models.UUIDField()
    package_type=models.CharField(max_length=16)
    countdown_data = models.TextField()
    status = models.BooleanField()


class Event(models.Model):
    event_id = models.UUIDField()
    card_id = models.UUIDField()
    client_id = models.UUIDField()
    client_name = models.CharField(max_length=32)
    event_type = models.CharField(max_length=16)
    date = models.DateField()
    start_time = models.TimeField()
    notes = models.TextField()
