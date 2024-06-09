from django import forms
from .models import PORTFOLIOITEM
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class FORM(UserCreationForm):

    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = PORTFOLIOITEM

        fields = ['email', 'phone_no', 'password1', 'password2']
