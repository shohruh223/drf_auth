from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Product, User


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ()


class UserCreateModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=55, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=55, min_length=8, write_only=True)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if password != confirm_password:
            raise ValidationError('This confirm password is wrong')
        attrs['password'] = make_password(password)
        validate_data = super().validate(attrs)
        return validate_data

    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'email', 'password', 'confirm_password')


class GetMeSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')