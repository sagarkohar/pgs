from django.db import models

# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=100)
    event_description=models.TextField()
    event_video=models.FileField(upload_to='Event_videos/')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


