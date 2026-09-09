from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name = "main"),
    path("details/<int:vac_id>/", views.vacancy_details, name = "vacancy_details"),
    path("category/<slug:cat_slug>/", views.category_by_slug, name = "category_by_slug")
]