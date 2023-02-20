from django.urls import path
from .views import *


urlpatterns = [
    path('allVacancy/', vacancy_output, name='allVacancy'),
    path('createVacancy/', AddVacancy.as_view(), name='createVacancy'),
    path('createUser/', register_request, name='createUser'),
]
