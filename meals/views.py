from rest_framework import viewsets
from .models import DailyMenu
from .serializers import DailyMenuSerializer

class DailyMenuViewSet(viewsets.ModelViewSet):
    queryset = DailyMenu.objects.all()
    serializer_class = DailyMenuSerializer