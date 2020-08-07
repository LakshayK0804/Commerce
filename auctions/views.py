from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listing
from .models import User
from django.views.generic import ListView, DetailView, CreateView
from .forms import ListingForm

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories(request):
    return render(request, "auctions/categories.html")

def cat_memes(request):
    return render(request, "auctions/memes.html")

def cat_gpus(request):
    return render(request, "auctions/gpus.html")

def cat_proc(request):
    return render(request, "auctions/proc.html")

def cat_ram(request):
    return render(request, "auctions/ram.html")

def cat_monitor(request):
    return render(request, "auctions/monitor.html")

def watchlist(request):
    return render(request, "auctions/watchlist.html")

class HomeView(ListView):
    model = Listing
    template_name = 'auctions/index.html'

class ArticleDetailView(DetailView):
    model = Listing
    template_name = 'auctions/listing_details.html'

class AddPostView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'auctions/form.html'
