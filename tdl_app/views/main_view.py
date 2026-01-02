from django.shortcuts import render, redirect, get_object_or_404
from ..models import todolist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index_view(request):
    if request.user.is_authenticated:
        tdl = todolist.objects.filter(user=request.user)
    else:
        tdl = []
    return render(request,'main/index.html',{'tasks': tdl})

@login_required
def add_task(request):
    errors = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if not title:
            errors['title'] = "Please Add Task Title."
        elif len(title) < 5 or len(title) > 50:
            errors['title'] = 'Title Cannot Less than 5 or More than 50.'

        if not description:
            errors['description'] = 'Please Add Description of Your Task.'
        
        if errors:
            return render(request, 'main/add_task.html', {'errors': errors, 'data': request.POST})
        
        else:
            tdl = todolist(
                title = title,
                description = description,
                user = request.user,
            ) 
            tdl.save()
            messages.success(request,'Task Added Successfully.')
            return redirect('index')
        
    return render(request,'main/add_task.html')

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(todolist, id = task_id, user = request.user)

    task.completed = not task.completed
    task.save()

    return redirect('index')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(todolist, id = task_id, user = request.user)

    task.delete()

    return redirect('index')