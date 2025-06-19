from django.shortcuts import render
from .models import Workout



# Create your views here.

def workouts_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workouts_list.html', {'workouts': workouts})


