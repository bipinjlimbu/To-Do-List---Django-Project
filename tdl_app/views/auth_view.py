from django.shortcuts import render

def login_view(request):
    return render(request,'auth/login_page.html')

def register_view(request):
    return render(request,'auth/register_page.html')
