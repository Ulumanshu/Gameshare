from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='User Name')
    password1 = forms.CharField(max_length=20, help_text=True, widget=forms.PasswordInput,
                                label='Password', error_messages={'required': 'field is required '})
    password2 = forms.CharField(max_length=20, help_text=True, widget=forms.PasswordInput,
                                label='Confirm password', error_messages={'required': 'field is required '})

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]