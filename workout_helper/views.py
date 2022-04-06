from django.shortcuts import render
from .models import Workout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def workouts(request):
    workouts = Workout.objects.all().order_by('id')
    paginator = Paginator(workouts, 12)
    page_num = request.GET.get('page', 1)
    workouts = paginator.get_page(page_num)
    context = {'workouts': workouts}
    return render(request, 'workout_helper/workouts.html', context)


@login_required(login_url='login')
def workoutDetails(request, pk):
    workout = Workout.objects.get(pk=pk)
    minor_muscle = workout.minor_muscle
    notes = workout.notes
    if(minor_muscle == None):
        minor_muscle = None
    else:
        minor_muscle = minor_muscle.split(',')

    if notes == None:
        notes = None
    else:
        notes = notes

    context = {
        'workout': workout,
        'equipment': workout.equipment.split(','),
        'exercise_type': workout.exercise_type.split(','),
        'major_muscle': workout.major_muscle.split(','),
        'minor_muscle': minor_muscle,
        'notes': notes,
    }
    return render(request, 'workout_helper/workoutDetails.html', context)
