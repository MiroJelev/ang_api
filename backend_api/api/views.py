from django.shortcuts import render
from backend_api.api.models import Country, City, Politics
from backend_api.api.serializers import CitySerializer, CountrySerializer, PoliticsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CountryList(APIView):
    serializer_class = CountrySerializer
    def get(self, request, format=None):
        sql_query = """SELECT * FROM Mondial.country
INNER JOIN Mondial.politics 
ON Mondial.country.Code=Mondial.politics.Country
INNER JOIN Mondial.encompasses
ON Mondial.country.Code=Mondial.encompasses.Country
WHERE (Government LIKE '%%monarch%%' 
OR Government LIKE '%%principality%%');"""

        countries = Country.objects.prefetch_related('politics').raw(sql_query)
        countries = Country.objects.prefetch_related('continents').raw(sql_query)
        countries = Country.objects.prefetch_related('economy').raw(sql_query)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
        
class PoliticsList(APIView):
    serializer_class = PoliticsSerializer
    def get(self, request, format=None):
        sql_query = """SELECT * FROM Mondial.politics
INNER JOIN Mondial.country 
ON Mondial.country.Code=Mondial.politics.Country
INNER JOIN Mondial.encompasses
ON Mondial.country.Code=Mondial.encompasses.Country
WHERE (Government LIKE '%%monarch%%' 
OR Government LIKE '%%principality%%')
AND Continent Like 'Europe';"""

        policies = Politics.objects.raw(sql_query)
        serializer = PoliticsSerializer(policies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class CountryCityList(APIView):
    serializer_class = CountrySerializer
    def get(self, request, format=None):
        if 'country_city' in request.query_params:
            country_city = request.query_params['country_city']
            if country_city is not None:
                countries = Country.objects.filter(name=country_city)
                serializer = CountrySerializer(countries, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response([], status.HTTP_204_NO_CONTENT)
        else:
            return Response([], status.HTTP_204_NO_CONTENT)