from rest_framework.serializers import ModelSerializer
from .models import Forum

class ForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'