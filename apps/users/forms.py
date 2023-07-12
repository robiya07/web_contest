from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUserModel


class RegistrationForm(UserCreationForm):
    INSTITUTION_CHOICES = [
        ('school', 'Школа'),
        ('kindergarten', 'Детский сад'),
        ('other', 'Другое'),
    ]

    inst = forms.ChoiceField(
        choices=INSTITUTION_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password1', 'password2', 'inst']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    gender = forms.ChoiceField(required=False, choices=[('female', 'Женский'), ('male', 'Мужской')])
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)
    address = forms.CharField(required=False)
    school = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    current_password = forms.CharField(required=False)
    new_password = forms.CharField(required=False)
    confirm_password = forms.CharField(required=False)


