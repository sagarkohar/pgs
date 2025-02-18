from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=50)
    class_picture=models.ImageField(upload_to='class_pictures/', blank=True)
    class_description=models.TextField(default="The first step for every child. We lovingly nurture them as they begin to explore and understand the beautiful world around them. Our nursery class features specially designed programs and assignments that enhance children's logical thinking and prepare them for future learning.")
    class_time=models.CharField(max_length=50)
    fees=models.FloatField()
