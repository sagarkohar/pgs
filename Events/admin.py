from django.contrib import admin

# Register your models here.
from Events.models import *

class EventAdmin(admin.ModelAdmin):
    list_display=('event_name','event_description','event_video')

admin.site.register(Event,EventAdmin)
