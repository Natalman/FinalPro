from django.shortcuts import render,get_object_or_404,redirect
from .models import Activities

def activities(request):
    activities = Activities.objects.order_by('name')
    return render(request,'Activities/activities.html', {'activities': activities})

def activity_detail(request, activity_pk):
    activity = get_object_or_404(Activities, pk=activity_pk);
    return render(request, 'Activities/activity_detail.html' , {'activity' : activity})

def add_act(request):
    if request.method == "POST":
        pk = request.POST.get('pk')
        activity = get_object_or_404(Activities, pk=pk)
        activity.InProgress = True
        activity.save()

    return redirect('activities')
