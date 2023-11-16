from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'travel_year',
            'image_url',
            'score',
            'touristic_point',
            'analysis'
        ]
        labels = {
            'name': 'Location',
            'travel_year': 'Travel Year',
            'image_url': 'Location Image',
            'score': 'Trippin Score',
            'touristic_point' : 'Highlight',
            'analysis': 'Analysis'
        }