from django.contrib import admin
from .models import Snippet

admin.site.site_header = 'Admin DashBoard'

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    list_filter = ('created',)
    change_list_template = 'admin/snippets/snippets_change_list.html'
admin.site.register(Snippet, SnippetAdmin)
