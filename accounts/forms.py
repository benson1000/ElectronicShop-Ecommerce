




from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils import timezone, timesince
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']
    
    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        instance.username = instance.email

        if commit:
            instance.save()
        return instance
    





