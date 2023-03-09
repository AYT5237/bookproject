from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
  template_name = 'list.html'
  model = Task
  context_object_name = 'tasks'
  # デフォルトではobject_list

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['tasks'] = context['tasks'].filter(user=self.request.user)

    searchInputText = self.request.GET.get('search') or ''
    if searchInputText:
      context['tasks'] = context['tasks'].filter(title__startswith=searchInputText)

    context['search'] = searchInputText
    return context
    # get_context_dataはListViewがもともと持っている。それを上書き（オーバーライド）する

class TaskDetail(LoginRequiredMixin, DetailView):
  template_name = 'detail.html'
  model = Task
  context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
  template_name = 'create.html'
  model = Task
  fields = ['title', 'description', 'bookimage', 'date']
  success_url = reverse_lazy('list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  template_name = 'update.html'
  model = Task
  fields = ['title', 'description', 'bookimage', 'date']
  success_url = reverse_lazy('list')

class TaskDelete(LoginRequiredMixin, DeleteView):
  template_name = 'delete.html'
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('list')
  context_object_name = 'task'

class ListLogin(LoginView):
  template_name = 'login.html'
  fields = '__all__'

  def get_success_url(self):
    return reverse_lazy('list')

class RegisterUser(FormView):
  template_name = 'register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('list')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super().form_valid(form)

