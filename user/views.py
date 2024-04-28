from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer


# 회원가입 뷰
# class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    # serializer_class = RegisterSerializer
##
class RegisterView(generics.CreateAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
##


# 로그인 뷰
# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # token = serializer.validated_data  # validate()의 리턴값인 token을 받아온다.
        # return Response({"token": token.key}, status=status.HTTP_200_OK)
##
class LoginView(generics.CreateAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
##
