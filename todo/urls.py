from django.urls import path
from . import views

urlpatterns = [
    path('api/todo/', views.get_todo),
    path('api/todo/add/', views.add_task),
    path('api/todo/delete/', views.delete_task),
    path('api/todo/update/', views.update_task),
]
