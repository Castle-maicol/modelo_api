from django.urls import path
from .views  import CompanyView

urlpatterns = [
    path("Companies/",CompanyView.as_view(), name='Companies_list')
]

