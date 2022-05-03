from django.urls import path
from .views import BookList, BookDetailView

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail')
]