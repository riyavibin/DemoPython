from django.contrib import admin

# Register your models here.

from django.contrib.admin import site

# Register your models here.
from . models import Department,Courses

admin.site.register(Department)
admin.site.register(Courses)