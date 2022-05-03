from django import forms

from book.models import Comment, Feedback


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