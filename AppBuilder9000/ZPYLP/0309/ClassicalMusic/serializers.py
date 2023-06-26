from rest_framework import serializers

from .models import Musician, Role, Composition, Track


class CompositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Composition
        fields = ['title', 'authors', 'instrumentation']
        # extra_kwargs = {'authors': {'required': False}, 'instrumentation': {'required': False}}
        depth = 1

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ['movement', 'release']
        # extra_kwargs = {'authors': {'required': False}, 'instrumentation': {'required': False}}
        depth = 1


class MusicianSerializer(serializers.ModelSerializer):
    # show the role NAME in the GET requests and accept it in POST requests.
    role = serializers.SlugRelatedField(
        queryset=Role.objects.all(), slug_field='role'
    )
    class Meta:
        model = Musician
        fields = ['name','sort_name','type','gender','role','Life_begin','Life_end', 'image_url', 'MBID']

        # set life_ended to optional, otherwise it will require a valid boolean and not accept null.
        optional_fields = ['life_ended', ]

        depth = 2


class DynamicSerializer(serializers.ModelSerializer):
    # A ModelSerializer that takes an additional `fields` argument that controls which fields should be displayed.
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are specified in the `fields` argument.
            exclude = set(fields)
            existing = set(self.fields)
            for field_name in existing & exclude:
                self.fields.pop(field_name)

class MusicianOptionsSerializer(DynamicSerializer):
    # show the role NAME in the GET requests and accept it in POST requests.
    role = serializers.SlugRelatedField(
        queryset=Role.objects.all(), slug_field='role'
    )

    class Meta:
        model = Musician
        fields = ['name','sort_name','type','gender','role','Life_begin','Life_end', 'image_url', 'composition_set', 'track_set', 'MBID']

        # set life_ended to optional, otherwise it will require a valid boolean and not accept null.
        optional_fields = ['life_ended', ]

        depth = 2