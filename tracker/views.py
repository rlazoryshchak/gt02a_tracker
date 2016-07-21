from django.shortcuts import render
from models import Point

def index(request, date):
    points = Point.objects.all()
    return render(request, 'index.html', {'points': points})