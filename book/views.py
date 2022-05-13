from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView

from book.models import Book, Comment, Feedback
from book.forms import CommentForm, FeedbackForm, UserRegisterForm, UserLoginForm


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
        context['comments'] = Comment.objects.filter(book__pk=self.kwargs.get('pk'))
        return context


class CreateCommentView(CreateView):
    """ Комментарии """
    model = Comment
    form_class = CommentForm
    template_name = 'book/detail.html'
    success_url = "/detail/{book_id}/"


def about(request):
    return render(request, 'book/about.html')


class CreateFeedbackView(FormView):
    """Обратная связь"""
    model = Feedback
    form_class = FeedbackForm
    template_name = 'book/contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'book/register.html', {"form": form})


def user_login(request):
    if request.POST:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'book/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')