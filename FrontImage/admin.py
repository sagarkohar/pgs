from django.contrib import admin

# Register your models here.

from FrontImage.models import Images


class ImagesAdmin(admin.ModelAdmin):
    list_display=('image',)
admin.site.register(Images,ImagesAdmin)