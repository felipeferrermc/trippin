from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

class PostDetailView(DetailView):
    model = Post
    template_name = 'locations/detail.html'
    context_object_name = 'location'
    pk_url_kwarg = 'location_id'

class PostListView(ListView):
    model = Post
    template_name = 'locations/index.html'
    context_object_name = 'location_list'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'locations/create.html'
    success_url = reverse_lazy('locations:index') 

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'locations/update.html'
    pk_url_kwarg = 'location_id'
    context_object_name = 'location'

    def get_success_url(self):
        return reverse_lazy('locations:detail', kwargs={'location_id': self.object.id})

    def get_object(self, queryset=None):
        location_id = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Post, pk=location_id)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'locations/delete.html'
    context_object_name = 'location'
    success_url = reverse_lazy('locations:index') 

    def get_object(self, queryset=None):
        location_id = self.kwargs.get('location_id')
        return get_object_or_404(Post, pk=location_id)
    
def create_Comment(request, location_id):
    location = get_object_or_404(Post, pk=location_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            location=location)
            comment.save()
            return HttpResponseRedirect(
                reverse_lazy('locations:detail', args=(location_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'location': location}
    return render(request, 'locations/comment.html', context)