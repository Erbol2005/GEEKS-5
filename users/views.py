from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import random
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from users.models import UserConfirmation
from users.serializers import RegisterSerializer, ConfirmSerializer, LoginSerializer


# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data, is_active=False)
#     confirm = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
#     return Response({'code': confirm.code})


class RegisterAPIView(ListCreateAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirm = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'code': confirm.code}, status=status.HTTP_201_CREATED)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сохраняем пользователя
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def confirm(request):
#     serializer = ConfirmSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code', None)
#     confirmation = get_object_or_404(UserConfirmation, code=code)
#     user = confirmation.user
#     user.is_active = True
#     user.save()
#     return Response({"status": 'success'}, status=200)


class ConfirmAPIView(ListCreateAPIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code', None)
        confirmation = get_object_or_404(UserConfirmation, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        return Response({"status": 'success'}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(serializer.validated_data)
#     if user is not None:
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         user.save()
#         return Response({"status": token.key}, status=200)
#     else:
#         return Response({"status": 'bad request'}, status=400)


class LoginAPIView(ListCreateAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"status": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"status": 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
