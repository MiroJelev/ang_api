from django.shortcuts import render
from django.http import JsonResponse
from backend_api.api.models import Country
from backend_api.api.serializers import CountrySerializer

# Create your views here.

def country_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return JsonResponse({
        'data': serializer.data
    })
