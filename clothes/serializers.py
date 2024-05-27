from rest_framework import serializers
from .models import Clothes

class MySerializer(serializers.Serializer):
    class Meta:
        model = Clothes
        fields = '__all__'