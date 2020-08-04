from django.contrib import admin
from .models import Snippet

admin.site.site_header = 'Admin DashBoard'

admin.site.register(Snippet, SnippetAdmin)
