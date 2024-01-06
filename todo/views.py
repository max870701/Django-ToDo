from django.shortcuts import redirect, get_object_or_404
from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')