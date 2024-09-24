from django.db import models

# Create your models here.

class AboutUs(models.Model):
    big_image = models.ImageField(upload_to='about_us/')
    small_image = models.ImageField(upload_to='about_us/')
    description = models.TextField()


class Parents(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="parent_image/",blank=True,default="parent_image/default.png")
    opnion=models.TextField()
    address=models.TextField()
    contact_number=models.CharField(max_length=15,default="9819464437")


class Book(models.Model):
    student_name=models.CharField(max_length=100)
    student_address=models.TextField()
    student_grade=models.CharField(max_length=20)
    contact_number=models.CharField(max_length=15)
    


