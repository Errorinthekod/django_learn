from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Vacancy, Category
# Create your views here.

vac_cats = {
    "languages": [
        {"id": 1, "name": "C", },
        {"id": 2, "name": "Go", },
        {"id": 3, "name": "C#", },
        {"id": 4, "name": "C++", },
        {"id": 5, "name": "CSS", },
        {"id": 6, "name": "HTML", },
        {"id": 7, "name": "Java", },
        {"id": 8, "name": "Ruby", },
        {"id": 9, "name": "Golang", },
        {"id": 10, "name": "Python", },
        {"id": 11, "name": "JavaScript", },
        {"id": 12, "name": "TypeScript", },
    ],

    "positions": [
        {"id": 1 , "name": "Dev Ops" , } ,
        {"id": 2 , "name": "Backend" , } ,
        {"id": 3 , "name": "Frontend" , } ,
        {"id": 4 , "name": "Developer" , } ,
        {"id": 5 , "name": "Team Lead" , } ,
        {"id": 6 , "name": "Data Analytics" , } ,
        {"id": 7 , "name": "Project Manager" , } ,
        {"id": 8 , "name": "Cybersecurity Specialist" , } ,
    ] ,

    "grades": [
        {"id": 1 , "name": "Intern" , } ,
        {"id": 2 , "name": "Junior" , } ,
        {"id": 3 , "name": "Middle" , } ,
        {"id": 4 , "name": "Senior" , } ,
        {"id": 5 , "name": "Architect" , } ,
    ]

}


header_menu = [
    {"name": "Categories", "url_name": "categories"},
    {"name": "About", "url_name": "about"},
]


vacancy_lst = [
    {"id": 1, "title": "Python developer", "company": "Devano", "is_active": True,
     "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")
     ,"description": "Vacancy for Python developer. Requirements are crazy"},
    {"id": 2, "title": "Python developer", "company": "Metalab", "is_active": True,
     "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")
     ,"description": "Vacancy for Python developer. Requirements are crazy"},
    {"id": 3, "title": "Python developer", "company": "T Company", "is_active": False,
     "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")
     ,"description": "Vacancy for Python developer. Requirements are crazy"},
    {"id": 4, "title": "Go developer", "company": "Retone", "is_active": True,
     "date": "2026-09-09", "requirements": ("Go", "Microservices", "Docker", "PostgreSQL")
     ,"description": "Vacancy for Go developer. Requirements are crazy"},
    {"id": 5, "title": "C# developer", "company": "KGAME", "is_active": True,
     "date": "2026-09-09", "requirements": (".NET", "nugget", "Docker", "PostgreSQL")
     ,"description": "Vacancy for C# developer. Requirements are crazy"}
]

def main(request):
    data = {
        "title": "Main Vacancy List",
        "menu": header_menu,
        "vacancy_list": vacancy_list,
    }
    return render(request, "vacancy/main.html", context=data)

# def vacancy_details(request, vac_id):
#     data = {
#         "title": "Vacancy Details",
#         "menu": header_menu,
#         "vac_selected": vac_id,
#     }
#     return render(request, "vacancy/vacancy_details.html", context = data)


def category_by_slug(request, cat_slug):
    data = {
        "title": "Categories",
        "menu": header_menu,
        "cat_slug": cat_slug,
    }
    return render(request, "vacancy/category_by_slug.html", context = data)


def vacancy_list(request):
    queryset = Vacancy.objects.all()
    data = {
        "title": "Vacancy List",
        "menu": header_menu,
        "vacancy_list": queryset,
    }
    return render(request, "vacancy/vacancy_list.html", context = data)

def vacancy_details(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk = pk)
    except Vacancy.DoesNotExist:
        raise Http404("No Vacancy matches the given query.")

    data = {
        "title": f"Vacancy {pk}",
        "vacancy": vacancy,
    }
    return render(
        request,
        "vacancy/vacancy_details.html",
        context = data
    )

def vacancy_filtered(request, filters):
    queryset = Vacancy.objects.filter(
        title__icontains = filters,
        # AND
        position__icontains = filters)
    data = {
        "title": "Vacancy Filtered",
        "filtered_vacancies": queryset,

    }
    return render(
        request,
        "vacancy/vacancy_filtered.html",
        context = data,
    )


def vacancy_by_slug(request, vac_slug):
    vacancy = get_object_or_404(Vacancy, slug = vac_slug)

    data = {
        "title": f"Vacancy {vac_slug}",
        "vacancy": vacancy,
        "vac_selected": 1,
    }

    return render(request, "vacancy/vacancy_by_slug.html", context = data)


def active_vacancies(request):
    queryset = Vacancy.actives.all()

    return render(request,
                  "vacancy/active_vacancies.html",
                  {"vacancies": queryset})

