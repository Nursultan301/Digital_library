from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from book.models import Book, Comment, Feedback
from book.forms import CommentForm, FeedbackForm


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


def about(request):
    return render(request, 'book/about.html')


def contact(request):
    return render(request, 'book/contact.html')


class CreateFeedbackView(FormView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'book/contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


