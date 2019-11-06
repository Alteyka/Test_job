from django.urls import path
from django.conf.urls import url
from . views import *

urlpatterns = [
    path('list_of_banks/', list_of_banks, name='list_of_banks_url'),
    path('list_of_banks/', AddBank.as_view(), name='add_bank_url'),
]
