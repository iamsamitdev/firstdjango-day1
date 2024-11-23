from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .todoSerializer import TodoSerializer

class TodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)