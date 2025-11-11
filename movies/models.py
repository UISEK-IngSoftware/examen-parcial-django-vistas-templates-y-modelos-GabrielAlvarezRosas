from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=100, null=False)
    director=models.CharField(max_length=100, null=False)
    release_date=models.DateField(null=False)
    genre=models.CharField(max_length=100, null=False)
    synopsis=models.TextField(max_length=200, null=False)


    def __str__(self):
        return self.title