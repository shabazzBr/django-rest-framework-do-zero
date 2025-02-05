from django.urls import path
from restapp.views import TodoListAndCreate, todo_detail_change_and_delete

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', todo_detail_change_and_delete)
]
