from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm
from .models import User


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


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            email = form.cleaned_data['email']
            Category = form.cleaned_data['Category']
            Starting_Bid = form.cleaned_data['Starting_Bid']
            Description = form.cleaned_data['Description']

            print(title,email,Category,Starting_Bid,Description)

    form = ContactForm()
    return render(request, 'auctions/form.html',{'form': form})
