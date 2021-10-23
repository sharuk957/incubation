from rest_framework.serializers import ModelSerializer
from .models import Incubation


class registrationlistserializer(ModelSerializer):
    class Meta:
        model = Incubation
        fields = '__all__'