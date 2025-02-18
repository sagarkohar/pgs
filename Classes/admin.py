from django.contrib import admin
from Classes.models import Classes

# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    list_display=['name','class_picture','class_time','fees','class_description']

admin.site.register(Classes,ClassAdmin)