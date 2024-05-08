# serializers.py

from rest_framework import serializers
from .models import UnitMenu, UserMealLike


class UnitMenuSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField()

    class Meta:
        model = UnitMenu
        fields = ['id', 'date', 'name', 'meal_type', 'like_count', 'liked']
        # fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request', None)
        if request and not request.user.is_authenticated:
            print('인증되지 않음; 좋아요 필드 배제')
            ret.pop('liked', None)  # 사용자가 인증되지 않은 경우 liked 필드를 제거
        return ret

    def get_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return UserMealLike.objects.filter(user=user, meal=obj).exists()
        return False


class UserMealLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMealLike
        # fields = ['id', 'user', 'meal', 'created_at']
        fields = '__all__'
