from django.shortcuts import render,get_object_or_404,redirect
from .models import Activities
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def MyActivities(request):
    Myact = Activities.objects.filter(InProgress=True)
    return render(request,'MyActivities/MyActivities.html', {'Myact': Myact})

@login_required
def delete_activity(request, pk):
    activities = get_object_or_404(Activities, pk=pk)
    activities.delete()
    return redirect('Trainer:MyActivities')
