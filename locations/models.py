from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.URLField(max_length=500, null=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    name = models.CharField(max_length=200)
    travel_year = models.IntegerField()
    image_url = models.URLField(max_length=500, null=True)
    score = models.CharField(max_length=3)
    touristic_point = models.CharField(max_length=200)
    analysis = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)



    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    location = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
