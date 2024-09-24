from django.contrib import admin

# Register your models here
from AboutUs.models import *

class AboutUsAdmin(admin.ModelAdmin):
    list_display=('description','big_image','small_image')

admin.site.register(AboutUs,AboutUsAdmin)

class ParentsAdmin(admin.ModelAdmin):
    list_display=('name','opnion','address','image')

admin.site.register(Parents,ParentsAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display=("student_name","student_grade","student_address","contact_number")

admin.site.register(Book,BookAdmin)