from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='todo_api'),  # Single API endpoint for all actions
]
