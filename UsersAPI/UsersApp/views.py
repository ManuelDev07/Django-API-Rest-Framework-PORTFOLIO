from django.shortcuts import render
from UsersApp.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from .models import UserProfile
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def user_profile_get_postAPIView(request):
    """Función APIView que se encargará de mostrar todos los datos de la API y crear los datos de un usuario nuevo.

    Args:
        request (object): HTTP method

    Returns:
        Response: Devolverá los datos de la API
    """

    if request.method == 'GET':
        #query
        user = UserProfile.objects.all()
        
        #serializer
        user_serializer = UserProfileSerializer(user, many=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        #serializo los datos recibidos
        user_serializer = UserProfileSerializer(data=request.data)

        if user_serializer.is_valid(): #si los datos son válidos
            user_serializer.save() #guardo los datos en la API

            return Response({'message':'User Created Successfully!','user':user_serializer.data}, status=status.HTTP_201_CREATED)
        
        else: #en caso de no ser válido la data
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_profile_get_put_deleteAPIView(request, id=None):
    """APIView que recibirá el id de un usuario para poder listar sus datos, actualizarlos o elimarlo por completo de la API.

    Args:
        request (object): HTTP method
        id (int, optional): Será el id del usuario con el que la API interactuará. Defaults to None.

    Returns:
        Response: Devolverá los datos de la API
    """
    
    #query
    user = UserProfile.objects.get(id=id)
    
    if user:#Si el usuario existe:

        if request.method == 'GET': #GET/RETRIEVE/PATCH
            #serialize data
            user_serializer = UserProfileSerializer(user)

            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT': #PUT
            user_serializer = UserProfileSerializer(user, data=request.data)

            if user_serializer.is_valid(): #si los datos son válidos
                user_serializer.save() #guardo los datos en la API

                return Response({'message':'User Updated Successfully!','user':user_serializer.data}, status=status.HTTP_200_OK)
            
            else: #en caso de no ser válido la data
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': #DELETE
            user.delete()

            return Response({'message':'User Deleted Successfully!'}, status=status.HTTP_202_ACCEPTED)
    
    else: #Caso contrario de que no se encuentre el usuario
        return Response({'message':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
