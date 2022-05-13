from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from book.models import Comment, Feedback


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'E-mail'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control ", 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Пароль'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'messages', 'book']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            "messages": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментария'}),
        }

        labels = {
            'name': '',
            'email': '',
            'messages': ''
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'full_name', 'email', 'messages']
        widgets = {
            "subject": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема'}),
            "full_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            "messages": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментария'}),
        }

        labels = {
            'subject': '',
            'full_name': '',
            'email': '',
            'messages': ''
        }
