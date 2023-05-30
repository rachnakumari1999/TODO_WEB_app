from django.shortcuts import render,redirect
from .models import Tasktodo

# Create your views here.

def task_list(request):
    tasks = Tasktodo.objects.all()
    return render(request, 'create.html', {'tasks': tasks})

def Create_task(request):
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        description=request.POST['description']
        date=request.POST['date']
        Tasktodo.objects.create(title=title,category=category,description=description,date=date)
        return redirect('task_list')
    tasks = Tasktodo.objects.all()
    return render(request, 'create.html', {'tasks': tasks})

def update_task(request, task_id):
    task = Tasktodo.objects.get(id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.category = request.POST.get('category')
        task.description = request.POST.get('description')
        task.date = request.POST.get('date')
        task.save()
        return redirect('task_list')
    return render(request, 'updates.html', {'task': task})

def edit_task(request,task_id):
    task = Tasktodo.objects.get(id=task_id)
    return render(request, 'updates.html', {'task': task})

def delete_task(request, task_id):
    task = Tasktodo.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')




