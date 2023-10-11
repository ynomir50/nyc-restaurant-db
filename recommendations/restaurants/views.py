from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import * 
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import *

class RestaurantListView(SingleTableView):
    model = Restaurant
    table_class = RestaurantTable
    template_name = 'restaurants/list.html'

def index(request):
    return render(request, "restaurants/index.html")

def about(request):
    return render(request, "restaurants/about.html")

#def list(request):
#    context = {
#        "restaurants":Restaurant.objects.all()
#    }
#    return render(request, "restaurants/list.html", context)