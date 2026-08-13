from django.urls import path
from home.views import first_view

urlpatterns = [
    path("view/", first_view),
]