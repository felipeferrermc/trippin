from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

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
        form = PostForm(request.POST)
        if form.is_valid():
            location_name = form.cleaned_data['name']
            location_travel_year = form.cleaned_data['travel_year']
            location_image_url = form.cleaned_data['image_url']
            location_score = form.cleaned_data['score']
            location_touristic_point = form.cleaned_data['touristic_point']
            location_analysis = form.cleaned_data['analysis']
            location = Post(name=location_name,
                        travel_year=location_travel_year,
                        image_url=location_image_url, score = location_score, touristic_point = location_touristic_point, analysis = location_analysis)
            location.save()
            return HttpResponseRedirect(
                reverse('locations:detail', args=(location.id, )))
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'locations/create.html', context)

def update_location(request, location_id):
    location = get_object_or_404(Post, pk=location_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            location.name = form.cleaned_data['name']
            location.travel_year = form.cleaned_data['travel_year']
            location.image_url = form.cleaned_data['image_url']
            location.score = form.cleaned_data['score']
            location.touristic_point = form.cleaned_data['touristic_point']
            location.analysis = form.cleaned_data['analysis']
            location.save()
            return HttpResponseRedirect(
                reverse('locations:detail', args=(location.id, )))
    else:
        form = PostForm(
            initial={
                'name': location.name,
                'travel_year': location.travel_year,
                'image_url': location.image_url,
                'score': location.score,
                'touristic_point': location.touristic_point,
                'analysis': location.analysis
            })

    context = {'location': location, 'form': form}
    return render(request, 'locations/update.html', context)


def delete_location(request, location_id):
    location = get_object_or_404(Post, pk=location_id)

    if request.method == "POST":
        location.delete()
        return HttpResponseRedirect(reverse('locations:index'))

    context = {'location': location}
    return render(request, 'locations/delete.html', context)