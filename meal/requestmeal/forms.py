from django import forms
from django.contrib.auth.models import User
from .models import Student, RequestAmount, DonateAmount
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    #email = forms.EmailField
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
        labels = {'MS': 'Meal Swipes', 'DD': 'Dining Dollars'}

class RequestForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['access']

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonateAmount
        fields = ['MS', 'DD', 'netid']
        labels = {'MS': 'Meal Swipes', 'DD': 'Dining Dollars'}

