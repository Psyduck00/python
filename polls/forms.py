from django import forms
from django.db import models
from .models import UserExtended

class UserForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = '__all__'

class NormalForms(forms.Form):
    pass
