# django rest framework libraries
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# models BaseApp
from .models import TodoListModel

# serializers BaseApp
from .serializers import TodoListSerializer

# Swagger utils
from drf_yasg.utils import swagger_auto_schema

# My Views.
@swagger_auto_schema(method='GET', operation_description='GET /tasks/ -> Obtener todas las Tareas.', responses={status.HTTP_200_OK:TodoListSerializer(many=True)})
@swagger_auto_schema(method='POST', operation_description='POST /tasks/ -> Registrar Nueva Tarea.', request_body=TodoListSerializer,  responses={status.HTTP_201_CREATED:TodoListSerializer, "mensaje":"Nueva Tarea Creada."})
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def todo_apiview(request):
    """APIView para listar toda la data ó para registrar/crear una nueva Tarea."""

    #queryset
    try:
        queryset = TodoListModel.objects.all()
    except TodoListModel.DoesNotExist:
        return Response({'mensaje':'No Existe Ninguna Lista de Tareas.'}, status=status.HTTP_404_NOT_FOUND)

    #GET Method    
    if request.method == 'GET':
        serializer_class = TodoListSerializer(queryset, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)

    #POST Method
    elif request.method == 'POST':
        serializer_class = TodoListSerializer(data=request.data)

        if serializer_class.is_valid(): # si los datos recibidos son correctos
            serializer_class.save() # se guarda la info
        
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else: # caso contrario
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='GET', operation_description='GET /tasks/{task_id}/ -> Obtener una Tarea mediante su ID.', responses={status.HTTP_200_OK:TodoListSerializer})    
@swagger_auto_schema(method='PUT', operation_description='PUT /tasks/{task_id}/ -> Actualizar una Tarea mediante su ID', request_body=TodoListSerializer)
@swagger_auto_schema(method='DELETE', operation_description='DELETE /tasks/{task_id}/ -> Eliminar una Tarea mediante su ID', responses={status.HTTP_204_NO_CONTENT:'La Tarea Ha Sido Eliminada.'})
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def todo_apiview_detail(request, task_id:int):
    """APIView para listar, actualizar o eliminar toda la data una Tarea en específico."""

    #query
    try:
        queryset = TodoListModel.objects.get(pk=task_id)
    except TodoListModel.DoesNotExist:
        return Response({'mensaje':'Tarea No Encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    # GET (Retrieve) Method
    if request.method == 'GET':
        serializer_class = TodoListSerializer(queryset)

        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # PUT Method
    elif request.method == 'PUT':
        serializer_class = TodoListSerializer(queryset, data=request.data)

        # verifico que los datos enviados sean correctos para actualizar
        if serializer_class.is_valid():
            serializer_class.save()

            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE Method
    elif request.method == 'DELETE':
        queryset.delete() # se elimina el objeto

        return Response({'mensaje':'La Tarea Ha Sido Eliminada.'}, status=status.HTTP_204_NO_CONTENT)