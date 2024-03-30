# serializers.py

from rest_framework import serializers
from .models import DailyMenu

class DailyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = ['date', 'breakfast_menu', 'lunch_menu_1', 'lunch_menu_2', 'lunch_menu_3']
