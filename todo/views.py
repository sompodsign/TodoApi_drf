from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoSerializer
from .models import Todo
import json

@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    return Response(todoSerializer(todos, many=True).data)


@api_view(['POST'])
def create_todo(request):
    data = json.loads(request.body)
    todo = Todo.objects.create(
        _id=int(data['highestId']),
        title=data['title'],
        date=data['date'],
        month=data['month'],
        year=data['year'],
    )
    todo.save()
    return Response({"details": "successfully created!"})


@api_view(['DELETE'])
def delete_todo(request, id):
    todo_to_delete = Todo.objects.get(_id=id)
    todo_to_delete.delete()
    return Response({"Details": "Successfully deleted"})
