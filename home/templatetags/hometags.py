from django import template
import home.views as views
from vacancy.models import Category

register = template.Library()

@register.simple_tag(name = "get_cats") # registration of tag: get_categories
def get_categories():
    return views.cats_db

@register.inclusion_tag('home/list_categories.html')
def show_categories(cat_selected = 0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}