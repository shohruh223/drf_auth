from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Product, User
from app.serializers import ProductModelSerializer, UserCreateModelSerializer, GetMeSerializers


class ProductView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )


class UserView(ListCreateAPIView):
    serializer_class = UserCreateModelSerializer
    queryset = User.objects.all()


class GetMeView(ListAPIView):
    serializer_class = GetMeSerializers
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeSerializers(user).data
        return Response(serializer_data)

