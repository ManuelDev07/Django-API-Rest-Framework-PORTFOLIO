from .serializers import CarBrandSerializer, ModelCarSerializer, CountriesSerializer
from rest_framework import status
from .models import CarBrandsModel, ModelCarModel, CountriesModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.
#Para los Países fabricantes de autos:
@api_view(['GET', 'POST'])
def countriesAPIView_get_post(request):
    """APIView del Modelo Countries"""
    
    if request.method == 'GET':
        #queryset:
        country = CountriesModel.objects.filter(state=True) 

        #serializer:
        country_serializer = CountriesSerializer(country, many=True)

        return Response(country_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        #serializar los datos recibidos:
        country_serializer = CountriesSerializer(data=request.data)

        if country_serializer.is_valid(): #si los datos son correctos
            country_serializer.save() #los guardo en la BBDD

            return Response({'message':'Country Created Succesfully!', 'Country':country_serializer.data}, status=status.HTTP_201_CREATED)

        else:
            return Response({'message':'An Error has happened!', 'Country':country_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def countriesAPIView_put_delete(request, slug=None):
        """APIView que recibirá el slug de un país para poder listar sus datos, actualizarlos o elimarlo por completo de la API."""

        #query:
        country = CountriesModel.objects.get(slug=slug)

        if country: #Si existe el país en la API
            if request.method == 'GET':
                #serializo los datos:
                country_serializer = CountriesSerializer(country)

                return Response(country_serializer.data, status=status.HTTP_200_OK)

            elif request.method == 'PUT':
                country_serializer = CountriesSerializer(country, data=request.data)

                if country_serializer.is_valid():
                    country_serializer.save()
                
                    return Response({'message':'Country Updated Successfully!', 'Country':country_serializer.data}, status=status.HTTP_200_OK)

                else:
                    return Response({'message':'An Error has happened!', 'Country':country_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
            elif request.method == 'DELETE':
                country.delete()
                return Response({'message':'Country Deleted Successfully!'}, status=status.HTTP_202_ACCEPTED)

        else:
            return Response({'message':'Country Not Found'}, status=status.HTTP_404_NOT_FOUND)

#Para las Marcas de Autos:
class CarBrandsViewSet(viewsets.ModelViewSet):
    """ViewSet para el Modelo CarBrandsModel"""
    serializer_class = CarBrandSerializer

    def get_queryset(self, id=None):
        
        if id is None: #Si no se pasa un id se mostrarán todos
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else: #si hay un id se mostrará el objeto al que le pertenece
            return self.get_serializer().Meta.model.objects.filter(state=True, id=id)
        
    def list_(self, request): #GET
        car_brand_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(car_brand_serializer.data, status=status.HTTP_200_OK)

    def create(self, request): #POST
        car_brand_serializer = self.serializer_class(data=request.data)

        if car_brand_serializer.is_valid(): #si los datos son correctos se guardan en la API
            car_brand_serializer.save()

            return Response({'message':'Car Brand Created Successfully!', 'Car Brand':car_brand_serializer.data}, status=status.HTTP_201_CREATED)

        else: #Caso contrario se devuelve un error
            return Response({'message':'An ERROR has happened','Car Brand':car_brand_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None): #PUT
        if self.get_queryset(id): #se llama al método para obtener el objeto a buscar
            car_brand_serializer = self.serializer_class(self.get_queryset(id), data=request.data) #se le pasa el id mas los nuevos datos ingresados

            if car_brand_serializer.is_valid(): #si los datos son validados se guardan
                car_brand_serializer.save()
            
                return Response({'message':'Car Brand Updated Successfully!','Car Brand':car_brand_serializer.data}, status=status.HTTP_200_OK)
            else: #caso contrario de haber errores ingresados
                return Response({'message':'An ERROR has happened','Car Brand':car_brand_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        else: #caso contrario de no existir
            return Response({'message':'Car Brand Not Found!'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, id=None): #DELETE
        #se obtiene el objeto a eliminar
        car_brand = self.get_queryset().filter(id=id)
        
        #si dicho objeto existe se elimina
        if car_brand:
            car_brand.state = False #paso el estado a False para no mostrarlo en la API pero seguirá existiendo en mi BBDD
            car_brand.save() #guardo los cambios
            
            return Response({'message':'Car Brand Deleted Successfully!'}, status=status.HTTP_202_ACCEPTED)
        else: #caso contrario de no existir
            return Response({'message':'Car Brand Not Found!'}, status=status.HTTP_404_NOT_FOUND)

#Para los Modelos de los Autos:
class ModelCarsViewSet(viewsets.ModelViewSet):
    """ViewSet para el modelo ModelCarsModel"""
    serializer_class = ModelCarSerializer

    def get_queryset(self, pk=None):
        
        if pk is None: #Si no se pasa un id se mostrarán todos
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else: #si hay un id se mostrará el objeto al que le pertenece
            return self.get_serializer().Meta.model.objects.filter(state=True, pk=pk)
        
    def list_(self, request): #GET
        model_car_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(model_car_serializer.data, status=status.HTTP_200_OK)

    def create(self, request): #POST
        model_car_serializer = self.serializer_class(data=request.data)

        if model_car_serializer.is_valid(): #si los datos son correctos se guardan en la API
            model_car_serializer.save()

            return Response({'message':'Model Car Registered Successfully!', 'Model Car':model_car_serializer.data}, status=status.HTTP_201_CREATED)

        else: #Caso contrario se devuelve un error
            return Response({'message':'An ERROR has happened','Model Car':model_car_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None): #PUT
        if self.get_queryset(pk): #se llama al método para obtener el objeto a buscar
            model_car_serializer = self.serializer_class(self.get_queryset(pk), data=request.data) #se le pasa el id mas los nuevos datos ingresados

            if model_car_serializer.is_valid(): #si los datos son validados se guardan
                model_car_serializer.save()
            
                return Response({'message':'Model Car Updated Successfully!','Model Car':model_car_serializer.data}, status=status.HTTP_200_OK)
            else: #caso contrario de haber errores ingresados
                return Response({'message':'An ERROR has happened','Model Car':model_car_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        else: #caso contrario de no existir
            return Response({'message':'Car Brand Not Found!'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None): #DELETE
        #se obtiene el objeto a eliminar
        model_car = self.get_queryset().filter(pk=pk)
        
        #si dicho objeto existe se elimina
        if model_car:
            model_car.state = False #paso el estado a False para no mostrarlo en la API pero seguirá existiendo en mi BBDD
            model_car.save() #guardo los cambios
            
            return Response({'message':'Model Car Deleted Successfully!'}, status=status.HTTP_202_ACCEPTED)
        else: #caso contrario de no existir
            return Response({'message':'Model Car Not Found!'}, status=status.HTTP_404_NOT_FOUND)