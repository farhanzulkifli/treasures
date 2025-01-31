from rest_framework import serializers
from .models import Treasure

class TreasuresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treasure
        fields = ('author', 'name','description', 'longitude','latitude','date','hunters')