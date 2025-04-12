from django.urls import path
from backend_api.api.views import CountryList

urlpatterns = [
    path('country/', CountryList.as_view())
]
