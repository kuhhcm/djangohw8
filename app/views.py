from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'create_todo.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'update_todo.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_list')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete_todo.html'
    success_url = reverse_lazy('todo_list')

