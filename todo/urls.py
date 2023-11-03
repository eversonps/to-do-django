from todo.views import TodoListCreate, TodoDeleteShowUpdate

from django.urls import path

urlpatterns = [
    # /todo
    path('', TodoListCreate.as_view()),
    # /todo/5
    path('/<int:pk>', TodoDeleteShowUpdate.as_view()),
]
