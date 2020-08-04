from django.contrib import admin
from .models import Snippet


# Register your models here.
admin.site.register(Snippet, SnippetAdmin)
admin.site.site_header = 'Admin DashBoard'

class SnippetAdmin(admin.ModelAdmin):
    fields = ('title',)
