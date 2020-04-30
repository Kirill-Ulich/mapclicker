from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.show_map),
    path('add_point/', csrf_exempt(views.add_point), name='add_point'),
    path('points_list/', views.points_list, name='points_list'),
]