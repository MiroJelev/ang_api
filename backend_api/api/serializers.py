from backend_api.api.models import Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name","code","capital","province","area","population"]
