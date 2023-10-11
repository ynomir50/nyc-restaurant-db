from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import * 


def index(request):
    return render(request, "restaurants/index.html")

def about(request):
    return render(request, "restaurants/about.html")

def list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, "restaurants/list.html", context)