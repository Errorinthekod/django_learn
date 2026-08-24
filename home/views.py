from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first(request):
    return HttpResponse("First view")


def dynamic(request, cat_id):
    return HttpResponse(f"<h1>Hello from dynamic view</h1><p>id: {cat_id}</p>")


def slug(request, cat_slug):
    return HttpResponse(f"<h1>Hello from slug view</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Hello from archive view</h1><p>year: {year}</p>")
