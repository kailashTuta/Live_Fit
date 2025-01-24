from django.core import validators
from django import forms
from .models import Post


class AddBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter Body', 'class': 'form-control'}),
        }
