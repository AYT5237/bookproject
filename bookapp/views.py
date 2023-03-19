from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import BookModel

# Create your views here.
class BookList(LoginRequiredMixin, ListView):
  template_name = 'list.html'
  model = BookModel
  context_object_name = 'books'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['books'] = context['books'].filter(user=self.request.user)

    searchInputText = self.request.GET.get('search') or ''
    if searchInputText:
      context['books'] = context['books'].filter(title__startswith=searchInputText)

    context['search'] = searchInputText
    return context

class BookDetail(LoginRequiredMixin, DetailView):
  template_name = 'detail.html'
  model = BookModel
  context_object_name = 'book'

class BookCreate(LoginRequiredMixin, CreateView):
  template_name = 'create.html'
  model = BookModel
  fields = ['title', 'description', 'bookimage', 'date']
  success_url = reverse_lazy('list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
  template_name = 'update.html'
  model = BookModel
  fields = ['title', 'description', 'bookimage', 'date']
  success_url = reverse_lazy('list')

class BookDelete(LoginRequiredMixin, DeleteView):
  template_name = 'delete.html'
  model = BookModel
  fields = '__all__'
  success_url = reverse_lazy('list')
  context_object_name = 'book'

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

