from django.shortcuts import render
from backend_api.api.models import Country
from backend_api.api.serializers import CountrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CountryList(APIView):
    serializer_class = CountrySerializer
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status.HTTP_200_OK)