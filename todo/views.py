from django.http import JsonResponse
from datetime import datetime

todo_list = []

def get_todo(request):
    return JsonResponse({"tasks": todo_list})

def add_task(request):
    message = request.GET.get('message', '')
    if message:
        task = {
            "message": message,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        todo_list.append(task)
    return JsonResponse({"tasks": todo_list})

def delete_task(request):
    index = int(request.GET.get('index', -1))
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    return JsonResponse({"tasks": todo_list})

def update_task(request):
    index = int(request.GET.get('index', -1))
    if 0 <= index < len(todo_list):
        todo_list[index]["message"] = request.GET.get('message', todo_list[index]["message"])
    return JsonResponse({"tasks": todo_list})
