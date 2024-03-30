# serializers.py

from rest_framework import serializers
from .models import UnitMenu, UserMealLike


class UnitMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMenu
        # fields = ['id', 'date', 'name', 'meal_type', 'like_count']
        fields = '__all__'


class UserMealLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMealLike
        # fields = ['id', 'user', 'meal', 'created_at']
        fields = '__all__'
