from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        label = {'text': 'Текст поста', 'group': 'Группа'}

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'})
        }
