from todo.views import TodoListCreate, TodoDeleteShowUpdate

from django.urls import path

urlpatterns = [
    # /todo
    path('todo', TodoListCreate.as_view()),
    # /todo/5
    path('todo/<int:pk>', TodoDeleteShowUpdate.as_view()),
]
