from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from django.forms.utils import ErrorList
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self,
                 *args,
                 **kwargs) -> None:
        super().__init__(*args,
                         **kwargs)
        self.fields['cat'].empty_label = "Not changed"

    class Meta:
        model = Exercises
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'content': forms.Textarea(attrs={
                'cols': 60,
                'rows': 10,
            })
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError(
                'The title is longer than 200 characters')
        return title
