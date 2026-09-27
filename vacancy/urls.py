from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name = "main"),
    path("category/<slug:cat_slug>/", views.category_by_slug, name = "category_by_slug"),
    path("list/", views.vacancy_list, name = "vacancy_list"),
    path("details/<int:pk>/", views.vacancy_details, name = "vacancy_details"),
    path("filtered/<str:filters>/", views.vacancy_filtered, name = "vacancy_filtered"),
    path("slug/<slug:vac_slug>/", views.vacancy_by_slug, name = "vacancy_by_slug"),
    path("actives/", views.active_vacancies, name = "active_vacancies"),


]