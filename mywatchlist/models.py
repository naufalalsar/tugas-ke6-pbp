from django.db import models

class myWatchList(models.Model):
    title = models.CharField(max_length=255)
    watched = models.CharField(max_length=3)
    rating = models.FloatField()
    release_date = models.CharField(max_length=50)
    review = models.TextField()
