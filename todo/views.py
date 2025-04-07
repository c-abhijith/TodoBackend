from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

todo_list = []

class TodoAPIView(APIView):

    def get(self, request):
        return Response({"tasks": todo_list}, status=status.HTTP_200_OK)

    def post(self, request):
        message = request.data.get('message', '')
        if message:
            task = {
                "message": message,
                "time": datetime.now().strftime("%H:%M:%S")
            }
            todo_list.append(task)
            return Response({"tasks": todo_list}, status=status.HTTP_201_CREATED)
        return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        index = request.data.get('index', -1)
        if 0 <= index < len(todo_list):
            todo_list.pop(index)
            return Response({"tasks": todo_list}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid index"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        index = request.data.get('index', -1)
        if 0 <= index < len(todo_list):
            message = request.data.get('message', todo_list[index]["message"])
            todo_list[index]["message"] = message
            return Response({"tasks": todo_list}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid index"}, status=status.HTTP_400_BAD_REQUEST)
