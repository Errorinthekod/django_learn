from django.shortcuts import render

# Create your views here.

header_menu = [
    {"name": "Categories", "url_name": "categories"},
    {"name": "About", "url_name": "about"},
]

vacancy_list = [
    {"id": 1, "title": "Python developer", "company": "Devano", "is_active": True, "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")},
    {"id": 2, "title": "Python developer", "company": "Metalab", "is_active": True, "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")},
    {"id": 3, "title": "Python developer", "company": "T Company", "is_active": False, "date": "2026-09-09", "requirements": ("Django", "FastAPI", "Docker", "PostgreSQL")},
    {"id": 4, "title": "Go developer", "company": "Retone", "is_active": True, "date": "2026-09-09", "requirements": ("Go", "Microservices", "Docker", "PostgreSQL")},
    {"id": 5, "title": "C# developer", "company": "KGAME", "is_active": True, "date": "2026-09-09", "requirements": (".NET", "nugget", "Docker", "PostgreSQL")},
]

def main(request):
    data = {
        "title": "Main Vacancy List",
        "menu": header_menu,
        "vacancy_list": vacancy_list,
    }
    return render(request, "vacancy/main.html", context=data)

def vacancy_details(request, vac_id):
    data = {
        "title": "Vacancy Details",
        "menu": header_menu,
        "vac_selected": vac_id,
    }
    return render(request, "vacancy/vacancy_details.html", context = data)