from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    errors = {}

    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        if not identifier:
            errors['identifier'] = 'Enter Your Username or Email.'

        if not password:
            errors['password'] = 'Enter Your Password.'

        if not errors:
            user = authenticate(request,username=identifier,password=password)
            if user is None:
                try:
                    check = User.objects.get(email=identifier)
                    user = authenticate(request, username=check.username, password=password)
                except User.DoesNotExist:
                    user = None
            
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfull.')
                return redirect('index')
            else:
                errors['general'] = 'Invalid Username/email or Password.'
        
    return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})

def register_view(request):
    errors = {}

    if request.method == 'POST':
        username = request.POST.get('username').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        confirm_password = request.POST.get('confirm_password').strip()

        if not username:
            errors['username'] = 'Enter Your Username.'
        elif len(username)<=3 or len(username)>=30:
            errors['username'] = 'Username Cannot be less than 3 or more than 30.'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Username is already taken.'

        if not first_name:
            errors['first_name'] = 'Enter Your First Name.'
        elif not first_name.isalpha():
            errors['first_name'] = 'First Name can only be in Alphabet.'
        elif len(first_name) > 30:
            errors['first_name'] = 'First Name cannot be more than 30.'

        if not last_name:
            errors['last_name'] = 'Enter Your Last Name.'
        elif not last_name.isalpha():
            errors['last_name'] = 'Last Name can only be in Alphabet.'
        elif len(last_name) > 30:
            errors['last_name'] = 'Last Name cannot be more than 30.'

        if not email:
            errors['email'] = 'Email is required.'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email is already registered.'

        if not password:
            errors['password'] = 'Enter Your Password.'
        elif len(password) < 6:
            errors['password'] = 'Password Needs to be More than 6.'
        
        if not confirm_password:
            errors['confirm_password'] = 'Confirm Your Password.'
        elif password != confirm_password:
            errors['general'] = 'Password does not match.'

        if errors:
            return render(request,'auth/register_page.html',{'errors':errors,'data':request.POST})
        else:
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
            )
            user.save()
            messages.success(request,'Registration Successfull. You can Login Now.')
            return redirect('login')
    
    else:
        return render(request,'auth/register_page.html')

def logout_view(request):
    logout(request)
    return redirect('index')