from rest_framework.serializers import ModelSerializer
from .models import Tarea #importamos modelo Tarea

class TareaSerializer(ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__' #para utilizar todos los campos
