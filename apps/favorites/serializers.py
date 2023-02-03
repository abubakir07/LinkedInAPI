from rest_framework import serializers

from apps.favorites.models import Favorite


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        read_only_fields = ('owner',)
        fields = (
            'id',
            'post',
        )
