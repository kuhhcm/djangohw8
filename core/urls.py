from django.urls import path, re_path
from app.views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    re_path(r'^task/(?P<pk>\d+)/$', TodoDetailView.as_view(), name='todo_detail'),
    path('task/create/', TodoCreateView.as_view(), name='todo_create'),
    re_path(r'^task/(?P<pk>\d+)/update/$', TodoUpdateView.as_view(), name='todo_update'),
    re_path(r'^task/(?P<pk>\d+)/delete/$', TodoDeleteView.as_view(), name='todo_delete'),
]
