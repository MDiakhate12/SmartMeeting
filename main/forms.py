from django.forms import ModelForm
from .models import Meeting
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django import forms

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'obj','points','members','chairperson','previous_meeting']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the meeting'}),
            'obj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Object of the meeting'}),
            'points': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Points of the meeting (Put commas " , " to separate points)'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'chairperson': forms.Select(attrs={'class': 'form-control'}),
            'previous_meeting': forms.Select(attrs={'class': 'form-control'}),
            'next_meeting': forms.Select(attrs={'class': 'form-control'}),
        }
