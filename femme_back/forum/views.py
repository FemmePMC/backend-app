from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ForumSerializer
from .models import Forum

@api_view(["GET"])
def getRoute(request):
    routes[
        {
            'Endpoint': '',
            'method': '',
            'id': None,
            'nombre': None,
            'tema': None,
            'users': None,
        }
    ]

"""
Obtenemos la informacion de todos los foros
"""
@api_view(['GET'])
def getForums(request):
    forum = Forum.objects.all()
    serializer = ForumSerializer(forum, many=True)
    return  Response(serializer.data)


"""
Obtenemos la informacion de un foro en especifico
"""
@api_view(['GET'])
def getForum(request, pk):
    forum = Forum.objects.get(id=pk)
    serializer = ForumSerializer(forum, many=False)
    return  Response(serializer.data)


"""
Agregamos un foro a la base de datos
"""
@api_view(['POST'])
def createForum(request):
    data = request.data
    forum = Forum.objects.create(
        id = data['id'],
        nombre = data['nombre'],
        tema = data['tema'],
        users = data['users']
    )
    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)


"""
Actualizamos la informacion de un foro en especifico
"""
@api_view(['PUT'])
def updateForum(request, pk):
    data = request.data
    forum = Forum.objects.get(id=pk)
    serializer = ForumSerializer(instance=forum, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Eliminamos un foro de la base de datos
"""
@api_view(['DELETE'])
def deleteForum(request, pk):
    forum = Forum.objects.get(id=pk)
    forum.delete()
    return Response('Foro eliminado!')
