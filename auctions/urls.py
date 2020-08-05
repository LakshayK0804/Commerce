from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("categories/memes", views.cat_memes, name="cat_memes"),
    path("categories/gpus", views.cat_gpus, name="cat_gpus"),
    path("categories/proc", views.cat_proc, name="cat_proc"),
    path("categories/ram", views.cat_ram, name="cat_ram"),
    path("categories/monitor", views.cat_monitor, name="cat_monitor"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("contact", views.contact, name="contact")
]
