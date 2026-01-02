from django.shortcuts import render

def index_view(request):
    return render(request,'main/index.html')

def add_task(request):
    return render(request,'main/add_task.html')