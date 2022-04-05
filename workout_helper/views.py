from django.shortcuts import render
from .models import Workout
from django.core.paginator import Paginator

# Create your views here.


def workouts(request):
    workouts = Workout.objects.all().order_by('-id')

    paginator = Paginator(workouts, 12)
    page_num = request.GET.get('page', 1)
    workouts = paginator.get_page(page_num)
    context = {'workouts': workouts}
    return render(request, 'workout_helper/workouts.html', context)
