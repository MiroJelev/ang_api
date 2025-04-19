from django.urls import path
from backend_api.api.views import CountryCityList, CountryList, PoliticsList

urlpatterns = [
    path('country/', CountryList.as_view()),
    path('policy/', PoliticsList.as_view()),
    path('country_cities/', CountryCityList.as_view())
]
