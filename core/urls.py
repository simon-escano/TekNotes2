from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('your_notes/', views.your_notes, name='your_notes'),
    path('likes/', views.likes, name='likes'),
    path('archive/', views.archive, name='archive'),
]