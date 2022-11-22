from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlertSerializer
from .models import Alert

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
Agregamos una alerta a la base de datos
"""
@api_view(['POST'])
def createAlert(request):
    data = request.data
    alert = Alert.objects.create(
        message = data['message'],
        user = data['user_id'],
    )
    serializer = AlertSerializer(alert, many=False)
    return Response(serializer.data)


"""
Elimina una alerta de la base de datos
"""
@api_view(['DELETE'])
def deleteAlert(request, pk):
    alert = Alert.objects.get(id=pk)
    alert.delete()
    return Response('Alerta eliminada')
