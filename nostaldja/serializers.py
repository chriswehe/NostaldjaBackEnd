from rest_framework import serializers

from .models import Decade, Fad

class FadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fad
        fields = ('name', 'image_url', 'description', 'decade', 'id')

class DecadeSerializer(serializers.ModelSerializer):

    fads = FadSerializer(many=True)

    class Meta:
        model = Decade
        fields = ('start_year', 'fads', 'id')