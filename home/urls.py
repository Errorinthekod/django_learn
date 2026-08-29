from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("login/", views.login, name = "login"),
    path("contact/", views.contact, name = "contact"),
    path("view/", views.first, name = "first"),
    path("dynamic_view/<int:cat_id>/", views.dynamic, name = "dynamic_id"),
    path("slug_view/<slug:cat_slug>/", views.slug, name = "slug"),
    path("post_view/<slug:cat_slug>/", views.post_request, name = "post"),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    path("archive/<year4:year>/", views.archive, name = "archive"),
    path("rndr_to_str/", views.rndr_to_str, name = "render_to_string"),
    path("rndr_html/", views.rndr_html, name = "render_html"),
    path("goods/", views.dataDB, name = "goods_html"),
    path("goods_id/<int:goods_id>/", views.show_goods, name = "show_goods_html"),

]