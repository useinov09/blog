from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {
            'title': 'Тема поста',
            'text': 'Описание',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название поста'}),
            'text': forms.Textarea(attrs={'placeholder': 'О чём вы хотите рассказать...'}),
        }

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].max_length = 15
        self.fields['username'].widget.attrs['maxlength'] = 15
        self.fields['username'].help_text = 'Не больше 20 символов.'