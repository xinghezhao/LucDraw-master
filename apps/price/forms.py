# -*- coding: utf-8 -*-
from django import forms
from .models import UserMessage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['image']