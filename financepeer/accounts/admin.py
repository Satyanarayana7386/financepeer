from django.contrib import admin
from accounts.models import UserData, Document

# Register your models here.

class AdminDisplay(admin.ModelAdmin):
    list_display = ('userId','title', 'body')

admin.site.register(UserData, AdminDisplay)
admin.site.register(Document)
