from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ForgetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ChangePasswordForm(forms.Form):
    current_p = forms.CharField(label='Current Password', max_length=100)
    new_p = forms.CharField(label='New Password', max_length=100)
    confirm_p = forms.CharField(label='Confirm Password', max_length=100)

