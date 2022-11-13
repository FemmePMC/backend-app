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
            'pasword': None,
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
        pasword = data['pasword'],
        name = data['name'],
        birth_date = data['birth_date'],
        photo = data['photo'],
        height = data['height'],
        email = data['email'],
        phone = data['phone'],
        location = data['location'],
        alerts_received = data['alerts_received'],
        emergency_contacts = data['emergency_contacts']
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

"""
Actualizamos el contenido de una persona
"""
@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
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