from datetime import datetime

from django import forms
from AuthenticationApp import models as auth_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    birthDate = forms.DateField(initial=datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = auth_model.User
        # fields = ('email', 'full_name')
        fields = ('email', 'full_name', 'phone_number', 'gender')

    def date_validate(self):
        birthDate = self.cleaned_data.get("birthDate")
        if birthDate >= datetime.today().date():
            return False
        return birthDate

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.birthDate = self.cleaned_data["birthDate"]
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = auth_model.User
        fields = ('email', 'password', 'birthDate', 'is_active', 'is_staff')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'email@emai.com'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'password'}))

    class Meta:
        model = auth_model.User
        fields = ['username', 'password']




class ImageUpdloadForm(forms.ModelForm):
    class Meta:
        model = auth_model.User
        fields = ['profile_pic']


class ProfileUpdateForm(forms.ModelForm):
    birthDate = forms.DateField(initial=datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = auth_model.User
        fields = ['full_name', 'birthDate', 'phone_number', 'gender']


class AdminProfileUpdateForm(forms.ModelForm):
    birthDate = forms.DateField(initial=datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = auth_model.User
        fields = ['id', 'email', 'full_name', 'phone_number', 'birthDate', 'is_staff', 'is_superuser', 'is_active']
