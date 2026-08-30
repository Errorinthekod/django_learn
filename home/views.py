from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string


menu = ["Main page", "About", "Login"]
main_menu = [
    {"name": "Login", "url_name": "login"},
    {"name": "Contact", "url_name": "contact"},
    {"name": "About", "url_name": "about"},
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

data_db = [
    {"id": 1, "title": "Goods 1", "description": """<h1>Lorem ipsum dolor</h1><p> sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. 
    Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna.  Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante.
    </p>""", "is_active": True},
    {"id": 2, "title": "Goods 2", "description": """<h1>Bounty belaying pin</h1><p> quarterdeck scuttle grog blossom red ensign hands pillage coxswain heave down. Pressgang long clothes walk the plank pirate driver parley heave down bilge execution dock overhaul. Crack Jennys tea cup scallywag Pirate Round rutters belay bowsprit bring a spring upon her cable Brethren of the Coast clap of thunder Jack Tar.
    Furl Buccaneer blow the man down take a caulk tender tackle booty lateen sail killick gangway. Hardtack main sheet crack Jennys tea cup parley fluke tackle Letter of Marque lookout carouser scuppers. Coffer grapple wench no prey, no pay keel lookout Yellow Jack scourge of the seven seas Blimey fire in the hole.
    Splice the main brace heave down hulk provost killick Letter of Marque bilge rat flogging grog blossom Chain Shot. Warp to go on account gaff scallywag line man-of-war hands crack Jennys tea cup weigh anchor Sink me. Tender bucko mutiny jury mast sutler snow hornswaggle yard fire ship gabion.
    </p>""", "is_active": False},
    {"id": 3, "title": "Goods 3", "description": """<h1>Silence Earthling.</h1><p> my name is Darth Vader. I'm am an extra-terrestrial from the planet Vulcan. No no no no no, Marty, both you and Jennifer turn out fine. It's your kids, Marty, something has got to be done about your kids. Great Scott. Let me see that photograph again of your brother. Just as I thought, this proves my theory, look at your brother. Well gee, I don't know. Marty, such a nice name.
    Hey Marty, I'm not your answering service, but you're outside pouting about the car, Jennifer Parker called you twice. Say that again. Calvin, why do you keep calling me Calvin? Marty, you didn't fall asleep, did you? I'm too loud. I can't believe it. I'm never gonna get a chance to play in front of anybody.
    Alright, okay listen, keep your pants on, she's over in the cafe. God, how do you do this? What made you change your mind, George? Yeah I know, If you put your mind to it you could accomplish anything. That Biff, what a character. Always trying to get away with something. Been on top of Biff ever since high school. Although, if it wasn't for him- I noticed you band is on the roster for dance auditions after school today. Why even bother Mcfly, you haven't got a chance, you're too much like your own man. No McFly ever amounted to anything in the history of Hill Valley. It was meant to be. Anyway, if Grandpa hadn't hit him, then none of you would have been born.
    </p>""", "is_active": True}
]

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
        "url": slugify("The main page"),

    }
    return render(request, "home/index.html", context=data)

def dataDB(request):
    data = {
        "title": "Goods",
        "main_menu": main_menu,
        "goods": data_db,
        "info": "Goods are good",
    }
    return render(request, "home/goods.html", context = data)


def show_goods(request, goods_id):
    return HttpResponse(f"Goods with id:{goods_id}")

def about(request):
    return render(request, "home/about.html", {"title": "About", "main_menu": main_menu})

def login(request):
    return HttpResponse("Login")

def contact(request):
    return HttpResponse("pywask")

