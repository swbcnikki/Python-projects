from rest_framework import serializers

from .models import *

class ImageSerializer(serializers.ModelSerializer):
   class Meta:
       model = Image
       fields = ('id', 'image_url')

class MeetupSerializer(serializers.ModelSerializer):

    image_url = serializers.CharField(source='image.image_url', read_only=True)

    class Meta:
        model = Meetup
        fields = ('id','name','description','meeting_time','location','postcode','contact','image_url')


