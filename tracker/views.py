from django.shortcuts import render
from models import Point

def index(request, date):
    return render(request, 'index.html', {'points': Point.by_day(date)})