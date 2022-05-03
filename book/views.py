from django.shortcuts import render
from django.views.generic import ListView, DetailView

from book.models import Book


class BookList(ListView):
    """Список книги"""
    model = Book
    template_name = 'book/index.html'


class BookDetailView(DetailView):
    """ Полное информации книги """
    model = Book
    template_name = "book/detail.html"
