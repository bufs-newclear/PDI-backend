
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnitMenuViewSet, DailyMenuViewSet

router = DefaultRouter()
router.register('meal', UnitMenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('daily/<date>', DailyMenuViewSet.as_view(), name='daily_menu')
]