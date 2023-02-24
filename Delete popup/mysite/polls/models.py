from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.TextField(blank=False)
    year = models.TextField(blank=False)
    filmurl = models.TextField(blank=False)
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre = models.TextField(blank=False)
    
    def __str__(self):
        return self.title