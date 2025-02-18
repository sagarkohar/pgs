from django.db import models

# Create your models here.

class Playing(models.Model):
    image=models.ImageField(upload_to="Gallery/playing/")


class Drawing(models.Model):
    image=models.ImageField(upload_to="Gallery/drawing/")

class Reading(models.Model):
    image=models.ImageField(upload_to="Gallery/reading/")
    
class Events(models.Model):
    image=models.ImageField(upload_to="Gallery/reading")