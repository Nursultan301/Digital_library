from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from book.models import Book, Comment
from book.forms import CommentForm


class BookList(ListView):
    """Список книги"""
    model = Book
    template_name = 'book/index.html'


class BookDetailView(DetailView):
    """ Полное информации книги """
    model = Book
    template_name = "book/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(pk=self.kwargs.get('pk'))
        return context


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'book/detail.html'
    success_url = '/'




