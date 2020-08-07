from django.contrib import admin

from .models import Listing

admin.site.site_header = 'Admin DashBoard'

admin.site.register(Listing)
