#Para trabajar con un APIView se importa lo siguiente:
from rest_framework.views import APIView #para crear mis distintas APIView heredando esta clase de Django
from rest_framework.response import Response #para devolver objetos response a doc JSON
from rest_framework import status
from profiles_api import serializers #import mis serializadores

#Para trabajar con los ViewSet se importa lo siguiente:
from rest_framework import viewsets

# Create your views here.
#Mostraré los datos de mi API mediante un APIView:
"""APIView CON FUNCIONES: es el mismo modo solo que la estructura al principio cambia al
declararse la funcion con el decorador, pero lo que va adentro de la función funciona de igual manera SOLO
si se verifca el método recibido con un if"""
from rest_framework.decorators import api_view #Importo el decorador

@api_view(['GET','POST']) #Declaro el método GET o POST o ambos
def hello_api_view_function(request):

    if request.method == 'GET':
        serializer_class = serializers.HelloSerializer

        list_apiview = [
            'Se trabajará con métodos HTTP como funciones (get, post, put, delete, patch)',
            'Es similar a una view tradicional de Django',
            'Da mayor control sobre lógica de mi APP',
            'Está mapeado manualmente a los URL',
            'Más texto de prueba'
        ]
    
    elif request.method == 'POST':

        #Se le pasan los datos a través del request con la clase del serializador del objeto instanciado y se almacenan en una variable
        serializer = serializer_class(data=request.data)

        if serializer.is_valid(): #Si es válido lo que se pasó se obtienen los datos 
            name = serializer.validated_data.get('name') #este 'name' entre () es el nombre de la variable creada en el serializador

            #Se envía un mensaje al crear el usuario (como un feedback):
            message = f'Hello {name}!'

            return Response({'message':message})

        else: #En caso de que los datos del formulario NO sean válidos:
            #Se devuelve un error y un BAD REQUEST 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""APIView con CLASES"""
class HelloApiView(APIView):
    #Debo colocar un docstring ya que se mostrará en la página al registrar su URL
    '''Esta clase será un view de API de prueba que mostrará un Hola Mundo con APIView'''
    
    #Cada método que haga (si trabaja con métodos HTTP) debe retornar un objeto Response
    #El Response permite que la info obtenida en el método se devuelva en formato JSON
    #Pero esa info que se pasará al Response debe ser una lista o un dict

    #También para importar mis serializadores debo instanciar un objeto de su clase:
    serializer_class = serializers.HelloSerializer

    #Creo la función GET: (se pasa un format=None)
    def get(self, request, format=None):
        '''Devolverá una lista de datos del APIView'''
         
        #Defino la lista:
        list_apiview = [
            'Se trabajará con métodos HTTP como funciones (get, post, put, delete, patch)',
            'Es similar a una view tradicional de Django',
            'Da mayor control sobre lógica de mi APP',
            'Está mapeado manualmente a los URL',
            'Más texto de prueba'
        ]

        return Response({'message':'Hello World!', 'my_apiview':list_apiview})

    #creo la función POST gracias a los serializadores que me pasarán los datos para agregarlos a la API
    def post(self, request):
        '''Crea un mensaje con el nombre del usuario registrado con el POST'''

        #Se le pasan los datos a través del request con la clase del serializador del objeto instanciado y se almacenan en una variable
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): #Si es válido lo que se pasó se obtienen los datos 
            name = serializer.validated_data.get('name') #este 'name' entre () es el nombre de la variable creada en el serializador

            #Se envía un mensaje al crear el usuario (como un feedback):
            message = f'Hello {name}!'

            return Response({'message':message})

        else: #En caso de que los datos del formulario NO sean válidos:
            #Se devuelve un error y un BAD REQUEST 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #El pk=id es para identificar el dato que se actualizará, en este caso no se usará un id, por lo que se establecerá como None
    def put(self, request, pk=None):
        '''Actualizará un dato de la API'''

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        '''Actualizará parcialmente un dato de la API'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''Eliminará por completo un dato de la API'''
        return Response({'method':'DELETE'})


#Mostraré los datos de mi API mediante un ViewSet:
class HelloViewSet(viewsets.ViewSet):
    '''API de prueba que se usará con ViewSet'''

    #Se usarán las distinas funciones que se usan con un ViewSet para acceder a mi API:
    
    #Para algunos métodos del ViewSet también se hace uso de los serializadores:
    serializer_class = serializers.HelloSerializer

    #Con list() devolverá ya sea un valor/mensaje en especifico, varios valores (un set de objetos)
    def list(self, request):
        '''Se devolverá un mensaje de Hola Mundo'''

        list_viewset = [
            'ViewSet usa acciones como: list, create, retrieve, update, partial_update',
            'Automáticamente mapea a los URLs usando Routers',
            'Provee más funcionalidad con menos código',
            'Más texto de prueba'
        ]

        #Como en los APIView, se debe retornar un objeto Response para mostrar un doc JSON:
        return Response({'message':'Hello World!', 'my_viewset':list_viewset})

    #Con create() se crearán nuevos datos para la API
    #Pero antes debo crearlo en mi serializador
    def create(self, request):
        '''Se crearán datos para la API'''

        #Básicamente se realiza casi mismo procedimiento que en la APIView

        #Se serializan los datos con el uso de la clase y se pasan los datos con el request.data
        serializer = self.serializer_class(data=request.data)

        #Luego se hace la misma verificación que con los APIView para chequear si los datos del formulario son válidos o no:
        if serializer.is_valid():
            #Se obtienen y almacenan los datos en una variable
            name = serializer.validated_data.get('name') #nombre del campo en el modelo

            message = f'Hola {name}!!'

            return Response({'message':message})
        
        else: #Mismo caso contrario por si los datos del formulario está erróneos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):
        '''Devolverá los datos de un objeto en específico de la API con su id'''

        return Response ({'http_method':'GET'}) #GET es el método que se utilizar al usar retrieve()

    #Esta función es la misma que usar PUT:
    def update(self, request, pk=None):
        '''Actualizará un dato en específico de la API'''

        return Response ({'http_method':'PUT'}) #PUT es el método que se utilizar al usar update()

    #Esta función es la misma que usar PATCH:
    def partial_update(self, request, pk=None):
        '''Actualizará parcialmente los datos de un objeto en específico de la API'''

        return Response ({'http_method':'PATCH'}) #PATCH es el método que se utilizar al usar partial_update()

    #Esta función es la misma que usar DELETE:
    def destroy(self, request, pk=None):
        '''Eliminará todos los datos de un objeto en específico de la API'''

        return Response ({'http_method':'DELETE'}) #DELETE es el método que se utilizar al usar partial_update()
