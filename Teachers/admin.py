from django.contrib import admin

# Register your models here.

from Teachers.models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','qualification','specialization','is_student','phone_number','profile_picture','email','address')

    admin.site.register(Teacher)