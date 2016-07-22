from django.shortcuts import render
from tracker.models import Point
from django.shortcuts import redirect


def index(request, date):
    if request.user.is_authenticated():
        return render(request, 'index.html', {'points': Point.by_day(date)})
    else:
        return redirect('/admin/')