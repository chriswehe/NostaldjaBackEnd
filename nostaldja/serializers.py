from rest_framework import serializers

from .models import Decade, Fad

class DecadeSerializer(serializers.ModelSerializer):
    fads = serializers.HyperlinkedRelatedField(
        view_name='fad_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Decade
        fields = ('start_year', 'fads',)


class FadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fad
        fields = ('name', 'image_url', 'description', 'decade',)