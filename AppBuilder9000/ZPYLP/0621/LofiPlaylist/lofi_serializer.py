from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


