from django import forms
from .models import *


class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["client_id", "name", "phone", "email"]


class FormPackage(forms.ModelForm):
    class Meta:
        model = Package
        fields = ["card_Id", "client_id", "package_type", "countdown_data", "status"]


class FormEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_id", "card_id", "client_id", "client_name", "event_type", "date", "start_time", "notes"]
