from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NombreSerializer
from .models import Nombre


"""
Se usa el framwork REST para facilitar el uso de la visualizacion de jsons
y poder usar los decoradores para los usos de las API'S
"""
@api_view(["GET"])
def getRoute(request):
    # Es un json con las rutas que vamos a usar dentro del proyecto
    routes = [
        {
            'Endpoint': '',
            'method': '',
            'body': None,
            'description': ''
        },
    ]
    return Response(routes)


"""
Serializamos para poder obtener la informacion de todas las personas
"""
@api_view(['GET'])
def getNombres(request):
    nombres = Nombre.objects.all()
    serializer = NombreSerializer(nombres, many=True)
    return  Response(serializer.data)

"""
Serializamos para poder obtener la informacion de una persona en especifico
"""
@api_view(['GET'])
def getNombre(request, pk):
    nombres = Nombre.objects.get(id=pk)
    serializer = NombreSerializer(nombres, many=False)
    return  Response(serializer.data)

"""
Serializamos para poder crear un nombre
"""
@api_view(['POST'])
def createNombre(request):
    data = request.data
    nombre = Nombre.objects.create(
        body = data['body']
    )
    serializer = NombreSerializer(nombre, many=False)
    return Response(serializer.data)

"""
Serializamos para poder actualizar el contenido de una persona
"""
@api_view(['PUT'])
def updateNombre(request, pk):
    data = request.data
    nombre = Nombre.objects.get(id=pk)

    serializer = NombreSerializer(nombre, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

"""
Eliminamos un nombre de la base de datos
"""
@api_view(['DEL'])
def deleteNombre(request, pk):
    nombre = Nombre.objects.get(id=pk)
    nombre.delete()
    return Response('Se elimino el nombre!')