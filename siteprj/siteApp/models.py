from django.db import models

# Create your models here.
class Sitedetails(models.Model):
    image=models.ImageField(upload_to='images')
    desc=models.TextField()
    name=models.TextField()
    rating=models.TextField()
    price=models.IntegerField()