from django.urls import path
from . import views

urlpatterns = [
        path('',views.main_page, name= 'main'),
        path('map/', views.map, name='map'),
        path('sightings/', views.sightings, name='sightings'),
        path('sightings/add/',views.add,name='add'),
        path('sightings/stats/', views.stats, name='stats'),
        path('sightings/<unique_squirrel_id>/',views.update,name='update'),

]


