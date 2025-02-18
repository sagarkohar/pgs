from django.db import models

# Create your models here.


class Teacher(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()
    profile_picture=models.ImageField(upload_to='teacher_pictures/')
    qualification=models.CharField(max_length=100)
    specialization=models.CharField(max_length=200)
    is_student=models.BooleanField(default=False)
    def __str__(self):
      return self.name
