from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer
from .models import Location

@api_view(['"GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '',
            'method': '',
            'latitud': None,
            'longitud': None,
            'zona': None,
            'description': ''
        },
    ]
    return Response(routes)

"""
obtenemos la informacion de la ubicacion que deseamos obtner
"""
@api_view(['GET'])
def getUbicacion(request,pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)


"""
Agregamos a la base de datos la informacion de la ubicacion
"""
@api_view(['POST'])
def createUbicacion(request):
    data = request.data
    location = Location.objects.create(
        latitude = data['latitude'],
        longitude = data['longitude'],
        zone = data['zone']
    )
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)

"""
Eliminamos la ubicacion que ya fue compartida 
"""
@api_view(['DELETE'])
def deleteUbicacion(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()
    return Response('Ubicacion eliminada');
