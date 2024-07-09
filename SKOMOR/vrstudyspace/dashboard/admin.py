from atexit import register
from tabnanny import verbose
from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)



