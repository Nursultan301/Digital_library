from django.urls import path
from .views import BookList, BookDetailView, CreateCommentView, about, CreateFeedbackView, register, user_login, \
    user_logout

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create-comment/', CreateCommentView.as_view(), name='create_comment'),
    path('about/', about, name='about'),
    path('contact/', CreateFeedbackView.as_view(), name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]