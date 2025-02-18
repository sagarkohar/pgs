from django.contrib import admin
from Gallery.models import *

# Register your models here.

class PlayingAdmin(admin.ModelAdmin):
    list_display=("image",)

class DrawingAdmin(admin.ModelAdmin):
    list_display=("image",)

class ReadingAdmin(admin.ModelAdmin):
    list_display=("image",)

class EventsAdmin(admin.ModelAdmin):
    list_display=("image",)

admin.site.register(Playing, PlayingAdmin)
admin.site.register(Drawing,DrawingAdmin)
admin.site.register(Reading,ReadingAdmin)
admin.site.register(Events,EventsAdmin)