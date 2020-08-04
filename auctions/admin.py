from django.contrib import admin
from .models import Snippet

# Register your models here.

admin.site.site_header = 'Admin Tutorial DashBoard'
admin.site.register(Snippet)
