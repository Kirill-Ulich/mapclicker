from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry

from .models import Point


def show_map(request):
    return render(request, 'map/map_clicker.html')


def add_point(request):
    geos_point = GEOSGeometry(f'POINT({request.POST["lat"]} {request.POST["lng"]})')
    point = Point(pointer=geos_point)
    point.save()
    return HttpResponse('')


def points_list(request):
    return render(request, 'map/points_list.html', {'points': Point.objects.all()})
