from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image","bio"]

class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name","last_name","username","email"]