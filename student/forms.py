from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['address','contact','profile_pic']