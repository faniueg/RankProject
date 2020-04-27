from rest_framework import serializers

from Rank.models import RankModels


class RankSerializers(serializers.ModelSerializer):
    class Meta:
        model = RankModels
        fields = ('id', 'grade', 'client', 'fraction')
