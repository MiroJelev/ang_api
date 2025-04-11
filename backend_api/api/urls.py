from django.urls import path
from backend_api.api.views import country_list

urlpatterns = [
    path('country/', country_list, name='country')
]
