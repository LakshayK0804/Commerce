from django.contrib import admin
from .models import Snippet
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = 'Admin DashBoard'

class SnippetAdmin(admin.ModelAdmin):
    fields = ('title','radio')

admin.site.register(Snippet)
admin.site.unregister(Group)
