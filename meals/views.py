from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UnitMenu
from .serializers import UnitMenuSerializer
from .permissions import HasEditPermission


class UnitMenuViewSet(viewsets.ModelViewSet):
    queryset = UnitMenu.objects.all()
    serializer_class = UnitMenuSerializer
    permission_classes = [HasEditPermission]


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
