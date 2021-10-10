from django.contrib import admin
from .models import *

# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display = ['user','time']

admin.site.register(Post,postadmin)
