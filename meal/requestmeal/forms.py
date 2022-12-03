from django import forms
from django.contrib.auth.models import User
from .models import Student, RequestAmount
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['access']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = RequestAmount
        fields = ['MS', 'DD']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['access']