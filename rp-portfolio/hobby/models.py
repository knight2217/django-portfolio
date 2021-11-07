from django.db import models

# Create your models here.
class Hobby(models.Model):
    Hobby_name = models.CharField(max_length=100)
    description = models.TextField()
    Type = models.CharField(max_length=20)
    image = models.FilePathField(path=r"C:\Users\vader227\Django\rp-portfolio\hobby\img")