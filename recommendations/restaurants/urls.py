from django.urls import path
from restaurants.views import RestaurantListView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name="about"),
    path("list/", RestaurantListView.as_view())
]