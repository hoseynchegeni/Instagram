from django.contrib import admin
from .models import *

# Register your models here.

class profileadmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(profile,profileadmin)
