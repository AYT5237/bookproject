from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, ListLogin, RegisterUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('login/', ListLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
] 

