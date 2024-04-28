
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnitMenuViewSet, DailyMenuViewSet, MealLikeViewSet, UserLikedMeals, MealLikeRankingView

router = DefaultRouter()
router.register('meal', UnitMenuViewSet)
router.register('like', MealLikeViewSet)
router.register('liked', UserLikedMeals, basename='user_liked')

urlpatterns = [
    path('', include(router.urls)),
    path('daily/<date>', DailyMenuViewSet.as_view(), name='daily_menu'),
    path('ranking', MealLikeRankingView.as_view(), name='like_ranking')
    # path('daily/<date>/<meal>/like', MealLikeViewSet.as_view({'get': 'create'}), name='daily_menu_like'),
    # path('liked', UserLikedMeals.as_view(), name='liked_menu'),
]
