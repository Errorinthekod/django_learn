from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = ["Main page", "About", "Login"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def first(request):
    return HttpResponse("First view")


def home(request):
    return HttpResponse("Home page")


def dynamic(request, cat_id):
    return HttpResponse(f"<h1>Hello from dynamic view</h1><p>id: {cat_id}</p>")


def slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Hello from slug view</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    # if year > 2026:
    #     raise Http404()

    # if year > 2026:
    #     return redirect("home", permanent=True) # 301 - permanent

    # if year > 2026:
    #     uri = reverse("slug", args=("music", ))
    #     return redirect(uri) # 302 - temporary

    # if year > 2026:
    #     uri = reverse("slug", args=("music", ))
    #     return HttpResponseRedirect(uri) # 302 - temporary
    #
    if year > 2026:
        uri = reverse("slug", args=("forever", ))
        return HttpResponsePermanentRedirect(uri) # 301 - permanent

    return HttpResponse(f"<h1>Hello from archive view</h1><p>year: {year}</p>")


def post_request(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Hello from slug view</h1><p>slug: {cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")


def rndr_to_str(request):
    r =  render_to_string("home/index.html")
    return HttpResponse(r)

def rndr_html(request):
    data = {
        "title": "index page",
        "str": "test string django",
        "question_str": "What is Django?",
        "price": 36,
        "menu": menu,
        "float": 3.14,
        "lst": [1, 2, 3, 'abc', True],
        "set": {"KG", "KZ", "UZ"},
        "dict": {
            "k1": "v1",
            "k2": "v2",
        },
        "obj": MyClass(10, 20),

    }
    return render(request, "home/index.html", context=data)