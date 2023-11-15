from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

def detail_location(request, location_id):
    location_data = Post.objects.all()
    location = get_object_or_404(Post, pk=location_id)
    context = {'location': location}
    return render(request, 'locations/detail.html', context)

def list_locations(request):
    location_data = Post.objects.all()
    context = {"location_list": location_data}
    return render(request, 'locations/index.html', context)

def create_location(request):
    if request.method == 'POST':
        location_name = request.POST['name']
        location_travel_year = request.POST['travel_year']
        location_image_url = request.POST['image_url']
        location_score = request.POST['score']
        location_touristic_point = request.POST['touristic_point']
        location_analysis = request.POST['analysis']
        location = Post(name=location_name,
                      travel_year=location_travel_year,
                      image_url=location_image_url, score = location_score, touristic_point = location_touristic_point, analysis = location_analysis)
        location.save()
        return HttpResponseRedirect(
            reverse('locations:detail', args=(location.id, )))
    else:
        return render(request, 'locations/create.html', {})

def update_location(request, location_id):
    location = get_object_or_404(Post, pk=location_id)

    if request.method == "POST":
        location.name = request.POST['name']
        location.travel_year = request.POST['travel_year']
        location.image_url = request.POST['image_url']
        location.score = request.POST['score']
        location.touristic_point = request.POST['touristic_point']
        location.analysis = request.POST['analysis']
        location.save()
        return HttpResponseRedirect(
            reverse('locations:detail', args=(location.id, )))

    context = {'location': location}
    return render(request, 'locations/update.html', context)


def delete_location(request, location_id):
    location = get_object_or_404(Post, pk=location_id)

    if request.method == "POST":
        location.delete()
        return HttpResponseRedirect(reverse('locations:index'))

    context = {'location': location}
    return render(request, 'locations/delete.html', context)