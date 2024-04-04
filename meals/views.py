from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UnitMenu, UserMealLike
from .serializers import UnitMenuSerializer, UserMealLikeSerializer
from .permissions import HasEditPermission
import logging


logger = logging.getLogger(__name__)
class UnitMenuViewSet(viewsets.ModelViewSet):
    queryset = UnitMenu.objects.all()
    serializer_class = UnitMenuSerializer
    permission_classes = [HasEditPermission]  ##PROD##


class DailyMenuViewSet(APIView):
    # queryset = DailyMenu.objects.all()
    # serializer_class = DailyMenuSerializer

    def get(self, request, date, format=None):
        try:
            # date 파라미터를 사용하여 해당 날짜의 식단 정보를 조회합니다.
            menus = UnitMenu.objects.filter(date=date)
            # Serializer를 사용하여 조회된 식단 정보를 JSON 형식으로 변환합니다.
            serializer = UnitMenuSerializer(menus, many=True)
            # 변환된 데이터를 Response 객체에 담아 반환합니다.
            return Response(serializer.data)
        except UnitMenu.DoesNotExist:
            # 해당 날짜의 식단 정보가 없는 경우 404 에러를 반환합니다.
            return Response(status=status.HTTP_404_NOT_FOUND)


class MealLikeViewSet(viewsets.ModelViewSet):
    queryset = UserMealLike.objects.all()
    serializer_class = UserMealLikeSerializer
    permission_classes = [IsAuthenticated]

    # 좋아요를 누를 때
    def create(self, request):
        if not request.user.is_authenticated:  ##PROD##
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        user = self.request.user

        # user = get_object_or_404(User, pk=int(request.data.get("user")))  ##DEV##
        meal_id = request.data.get("meal")
        if not meal_id:
            return Response({"error": "meal_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            meal_id = int(meal_id)
        except ValueError:
            return Response({"error": "Invalid meal_id"}, status=status.HTTP_400_BAD_REQUEST)

        # 이미 좋아요를 눌렀는지 확인
        meal = get_object_or_404(UnitMenu, pk=meal_id)
        existing_like = UserMealLike.objects.filter(user=user.id, meal=meal_id).first()  # noqa: E501

        if existing_like:
            # 이미 좋아요를 누른 상태에서 다시 누르면 좋아요 취소
            existing_like.delete()
            # Meal 모델의 like_count 감소
            Meal = get_object_or_404(UnitMenu, pk=meal_id)
            Meal.like_count -= 1
            Meal.save()
            return Response({"message": "좋아요 취소됨"}, status=status.HTTP_200_OK)
        else:
            # 좋아요를 누르지 않은 상태에서 누르면 좋아요 추가
            like_data = {"user": user.id, "meal": meal_id}
            serializer = self.get_serializer(data=like_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Meal 모델의 like_count 증가
            Meal = get_object_or_404(UnitMenu, pk=meal_id)
            Meal.like_count += 1
            Meal.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLikedMeals(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  ##PROD##

    def list(self, request):
        user = self.request.user  ##PROD##
        liked_Meals = UserMealLike.objects.filter(user=user).values_list('meal', flat=True)  # noqa: E501
        Meals = UnitMenu.objects.filter(id__in=liked_Meals)
        serializer = UnitMenuSerializer(Meals, many=True)
        return Response(serializer.data)
