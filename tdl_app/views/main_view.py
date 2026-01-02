from django.shortcuts import render, redirect
from ..models import todolist
from django.contrib import messages

def index_view(request):
    if request.user.is_authenticated:
        tdl = todolist.objects.filter(user=request.user)
    else:
        tdl = []
    return render(request,'main/index.html',{'tasks': tdl})

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