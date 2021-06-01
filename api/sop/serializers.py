from rest_framework import serializers
from .models import Meter

class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = ('iter', 'value')