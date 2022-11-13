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
            'body': None,
            'description': ''
        },
    ]
    return Response(routes)


"""
Serializamos para poder obtener la informacion de todas las personas
"""
@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return  Response(serializer.data)

"""
Serializamos para poder obtener la informacion de una persona en especifico
"""
@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return  Response(serializer.data)

"""
Serializamos para poder crear un nombre
"""
@api_view(['POST'])
def createUser(request):
    data = request.data
    user = User.objects.create(
        body = data['body']
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

"""
Serializamos para poder actualizar el contenido de una persona
"""
@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

"""
Eliminamos un nombre de la base de datos
"""
@api_view(['DEL'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('Se elimino el usuario!')