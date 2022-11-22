from alert.models import Alert
from alert.serializers import AlertSerializer
from location.models import Location
from location.serializers import LocationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


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
            'id_number': None,
            'id_type': None,
            'nickname': None,
            'password': None,
            'name': None,
            'birth_date': None,
            'photo': None,
            'height': None,
            'email': None,
            'phone': None,
            'location': None,
            'alerts_received': None,
            'emergency_contacts': None,
            'description': ''
        },
    ]
    return Response(routes)


"""
obtenemos la informacion de todas las personas
"""
@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return  Response(serializer.data)

"""
obtenemos la informacion de una persona en especifico
"""
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return  Response(serializer.data)

"""
Agregamos un nombre a la base de datos
"""
@api_view(['POST'])
def createUser(request):
    data = request.data
    user = User.objects.create(
        id_number = data['id_number'],
        id_type = data['id_type'],
        nickname = data['nickname'],
        password = data['password'],
        name = data['name'],
        birth_date = data['birth_date'],
        photo = data['photo'],
        height = data['height'],
        email = data['email'],
        phone = data['phone'],
        location_id = data['location_id']
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

"""
Actualizamos el contenido de una persona
"""
@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
    print(data)
    user = User.objects.get(id=pk)

    serializer = UserSerializer(user, data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

"""
Eliminamos un nombre de la base de datos
"""
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('Se elimino el usuario!')

"""
Patch es para actualizar solo un campo
"""
@api_view(['PATCH'])
def patchUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


"""
Obtener todos los usuarios relacionados a un usuario
"""
@api_view(['GET'])
def getRelatedUsers(request, pk):
    user = User.objects.get(id=pk)
    related_users = user.emergency_contacts.all()
    serializer = UserSerializer(related_users, many=True)
    return Response(serializer.data)

"""
Relacionar un usuario con otro
"""
@api_view(['POST'])
def relateUser(request, pk, pk2):
    user = User.objects.get(id=pk)
    user2 = User.objects.get(id=pk2)
    user.emergency_contacts.add(user2)
    return Response('Se relacionaron los usuarios')


"""
Relacionar una alerta a un usuario
"""
@api_view(['POST'])
def relateAlert(request, pk, pkAlert):
    user = User.objects.get(id=pk)
    alert = Alert.objects.get(id=pkAlert)
    user.alerts_received.add(alert)
    return Response('Se agrego la alerta correctamente')

"""
Obtener todas las alertas relacionadas a un usuario
"""
@api_view(['GET'])
def getRelatedAlerts(request, pk):
    user = User.objects.get(id=pk)
    related_alerts = user.alerts_received.all()
    serializer = AlertSerializer(related_alerts, many=True)
    return Response(serializer.data)

"""
Cambiar la latidud y longitud de una ubicación relacionada a un usuario
"""
@api_view(['PATCH'])
def patchRelatedLocation(request, pk):
    user = User.objects.get(id=pk)
    location = user.location
    data = request.data
    location.latitude = data['latitude']
    location.longitude = data['longitude']
    location.save()
    return Response('Se actualizo la ubicación correctamente')

"""
Obtener la ubicación relacionada a un usuario
"""
@api_view(['GET'])
def getRelatedLocation(request, pk):
    user = User.objects.get(id=pk)
    location = user.location
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)
