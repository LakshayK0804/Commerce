from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
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
    path('listing/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_listing', AddPostView.as_view(), name="add_post"),
    path('listing/edit/<int:pk>', UpdatePostView.as_view(), name='update_post')
]
