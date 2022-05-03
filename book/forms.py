from django import forms

from book.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'messages']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            "messages": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментария'})
        }

        labels = {
            'name': '',
            'email': '',
            'messages': ''
        }