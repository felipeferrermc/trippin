from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('<int:location_id>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<int:location_id>/', views.UpdatePostView.as_view(), name='update'),
    path('delete/<int:location_id>/', views.DeletePostView.as_view(), name='delete'),
    path('<int:location_id>/comment/', views.create_Comment, name='comment'),
]