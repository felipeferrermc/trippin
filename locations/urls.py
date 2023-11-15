from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.list_locations, name='index'),
    path('create/', views.create_location, name='create'),
    path('<int:location_id>/', views.detail_location, name='detail'),
    path('update/<int:location_id>/', views.update_location, name='update'),
    path('delete/<int:location_id>/', views.delete_location, name='delete'),
]