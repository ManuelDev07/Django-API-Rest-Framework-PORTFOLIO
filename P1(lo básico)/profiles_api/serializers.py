#Este será mi archivo de serializadores para mi API:
#Es buena práctica mantener todos mis serializadores dentro de un archivo dentro de mi APP para así tenerlos todos en un solo lugar.

from rest_framework import serializers

#Defino mis serializadores mediantes clases:
class HelloSerializer(serializers.Serializer):
    '''Se serializará un campo de prueba para mi APIView de pruebas'''
    #Se crea un campo:
    name = serializers.CharField(max_length=15)