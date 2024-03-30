from rest_framework import permissions


class HasEditPermission(permissions.BasePermission):
    """
    'Editors' 그룹의 사용자에게만 POST 요청을 허용하고,
    다른 모든 요청은 읽기 전용으로 처리합니다.
    """

    def has_permission(self, request, view):
        # 모든 사용자에게 읽기 권한 부여
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST 요청인 경우 'Editors' 그룹 소속 여부 확인
        return request.user.groups.filter(name='Editor').exists()
