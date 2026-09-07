from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name = "main"),
    path("details/<int:vac_id>/", views.vacancy_details, name = "vacancy_details"),

]