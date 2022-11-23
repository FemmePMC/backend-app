from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlertSerializer
from .models import Alert
from user.models import User
from user.serializers import UserSerializer

@api_view(['"GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '',
            'method': '',
            'message': None,
            'user': None,
            'description': ''
        }
    ]
    return Response(routes)

"""
obtenemos la informacion de la alerta que deseamos obtner
"""
@api_view(['GET'])
def getAlert(request, pk):
    alert = Alert.objects.get(id=pk)
    serializer = AlertSerializer(alert, many=False)
    return Response(serializer.data)


"""
Agregamos una alerta a la base de datos y la relacionamos con un usuario y los usuarios que estan relacionados con el usuario
"""
@api_view(['POST'])
def createAlert(request):
    data = request.data
    alert = Alert.objects.create(
        message = data['message'],
        user_id = data['user_id'],
    )
    serializer = AlertSerializer(alert, many=False)
    user = User.objects.get(id=data['user_id'])
    related_users = user.emergency_contacts.all()
    for user in related_users:
        user.alerts_received.add(alert)
        user.save()
    return Response(serializer.data)


"""
Elimina una alerta de la base de datos
"""
@api_view(['DELETE'])
def deleteAlert(request, pk):
    alert = Alert.objects.get(id=pk)
    alert.delete()
    return Response('Alerta eliminada')
