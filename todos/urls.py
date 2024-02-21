from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.todo_list, name="main"),
    path('insert_todo/',views.insert_todo_items,name="insert"),
    path('delete_todo/<int:todo_id>',views.delete_todo_items, name="delete")
]