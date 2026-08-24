from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("view/", views.first),
    path("dynamic_view/<int:cat_id>/", views.dynamic),
    path("slug_view/<slug:cat_slug>/", views.slug),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    path("archive/<year4:year>/", views.archive)
]