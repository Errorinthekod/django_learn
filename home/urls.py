from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.home, name = "home"),
    path("view/", views.first, name = "first"),
    path("dynamic_view/<int:cat_id>/", views.dynamic, name = "dynamic_id"),
    path("slug_view/<slug:cat_slug>/", views.slug, name = "slug"),
    path("post_view/<slug:cat_slug>/", views.post_request, name = "post"),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    path("archive/<year4:year>/", views.archive, name = "archive")
]