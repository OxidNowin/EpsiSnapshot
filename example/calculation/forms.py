import os
from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'file',)