from django import forms
from django.forms import ModelForm
from .models import Buyer

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"

    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
        "mail": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
        "phone_number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter your phone number"}),
        "home_address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your home address"}),
    }
