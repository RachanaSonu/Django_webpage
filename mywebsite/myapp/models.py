from django.utils import timezone
from django.db import models

# Create your models here.
class Cdata(models.Model):
    Instructor=models.CharField(max_length=50)
    Program_Language=models.CharField(max_length=50)
    Duration_Months=models.IntegerField()
    Start_Date=models.DateField()
    End_Date=models.DateField()
    Fee=models.IntegerField()


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='gallery_images/')
    designation = models.CharField(max_length=255, blank=True)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - Rating: {self.rating}"