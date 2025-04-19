from backend_api.api.models import Encompasses, Country, City, Politics
from rest_framework import serializers

class ContinentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encompasses
        fields = "__all__"

class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politics
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    politics = PoliticsSerializer()
    continents = ContinentsSerializer()
    class Meta:
        model = Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"