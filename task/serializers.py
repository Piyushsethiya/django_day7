from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class categoryserializers(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()

class meta:
    fields = ['url', 'username', 'email', 'is_staff']