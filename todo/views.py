from todo.models import Todo
from todo.serializers import TodoSerializer

import rest_framework.status as status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

# /todo 
class TodoListCreate(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# todo/2
class TodoDeleteShowUpdate(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()
        
    def get(self, request, pk):        
        serializer = TodoSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        serializer = TodoSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    