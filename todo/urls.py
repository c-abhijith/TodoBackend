from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.get_todo),
    path('todo/add/', views.add_task),
    path('todo/delete/', views.delete_task),
    path('todo/update/', views.update_task),
]
