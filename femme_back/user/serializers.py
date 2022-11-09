from rest_framework.serializers import ModelSerializer
from .models import Nombre

class NombreSerializer(ModelSerializer):
    class Meta:
        model = Nombre
        fields = '__all__'