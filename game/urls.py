from django.urls import path
from . import views

urlpatterns = [
    path('', views.wordle, name='wordle'),
    path('api/check/', views.check_guess, name='check_guess'),
    path('new/', views.new_game, name='new_game'),
] 