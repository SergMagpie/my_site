from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from django.forms.utils import ErrorList
from .models import *
from django.contrib.auth.forms import UserCreationForm


class AddPostForm(forms.ModelForm):
    def __init__(self,
                 *args,
                 **kwargs) -> None:
        self.author = kwargs['initial']['author']
        super().__init__(*args,
                         **kwargs)
        self.fields['cat'].empty_label = "Not changed"

    def save(self, commit=True):
        obj = super(AddPostForm, self).save(False)
        obj.author = self.author
        commit and obj.save()
        return obj

    class Meta:
        model = Exercises
        fields = '__all__'
        exclude = ['slug', 'author']

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


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
