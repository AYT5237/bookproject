from django.contrib import admin
from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete, ListLogin, RegisterUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', BookList.as_view(), name='list'),
    path('detail/<int:pk>/', BookDetail.as_view(), name='detail'),
    path('create/', BookCreate.as_view(), name='create'),
    path('book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    path('login/', ListLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
] 

