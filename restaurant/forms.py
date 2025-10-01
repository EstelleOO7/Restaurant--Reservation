from django.forms import ModelForm
from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'assigned_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # calendar widget
                'class': 'form-control'
            }),
            'number_of_hours': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional',
                'min': 1,
                'max': 24,
            }),
        }

