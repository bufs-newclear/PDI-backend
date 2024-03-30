# serializers.py

from rest_framework import serializers
from .models import UnitMenu


class UnitMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMenu
        fields = ['date', 'name', 'meal_type']
