from django.urls import path
from .views import BookList, BookDetailView, CreateCommentView, about, contact, CreateFeedbackView

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create-comment/', CreateCommentView.as_view(), name='create_comment'),
    path('about/', about, name='about'),
    path('contact/', CreateFeedbackView.as_view(), name='contact'),
]