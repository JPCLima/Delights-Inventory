from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
