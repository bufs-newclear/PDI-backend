
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyMenuViewSet

router = DefaultRouter()
router.register('meal', DailyMenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]