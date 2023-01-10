from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
