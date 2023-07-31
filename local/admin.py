from django.contrib import admin
from .models import Course_detail

# Register your models here.

class Course_detailAdmin(admin.ModelAdmin):
    models=Course_detail
    list_display=['Coursename','Code','Collage','Student']
admin.site.register(Course_detail,Course_detailAdmin)
