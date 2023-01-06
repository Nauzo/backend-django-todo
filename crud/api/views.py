from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers

#importaciones
from .models import Tarea
from .serializers import TareaSerializer

@api_view(['GET'])
def getTarea(request):
    tarea = Tarea.objects.all().order_by('-id')
    serializers = TareaSerializer(tarea, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def postTarea(request):
    data = request.data
    tarea = Tarea.objects.create(
        body = data['body']
    )
    serializers = TareaSerializer(tarea, many=False)
    return Response(serializers.data)

@api_view(['PUT'])
def putTarea(request, pk):
    data = request.data
    tarea = Tarea.objects.get(id=pk)
    serializer = TareaSerializer(instance=tarea, data=data)
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
def deleteTarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return Response(status=200)