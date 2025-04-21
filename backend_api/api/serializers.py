from backend_api.api.models import Encompasses, Country, City, Politics, Economy
from rest_framework import serializers

class EconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Economy
        fields = "__all__"

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
    economy = EconomySerializer()
    class Meta:
        model = Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"