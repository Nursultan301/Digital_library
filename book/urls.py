from django.urls import path
from .views import BookList, BookDetailView, CreateCommentView

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create-comment/', CreateCommentView.as_view(), name='create_comment'),
]