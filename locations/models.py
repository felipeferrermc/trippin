from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=200)
    travel_year = models.IntegerField()
    image_url = models.URLField(max_length=500, null=True)
    score = models.CharField(max_length=3)
    touristic_point = models.CharField(max_length=200)
    analysis = models.CharField(max_length=500)



    def __str__(self):
        return f'{self.name}'
