from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('/auth/signup')

        try:
            User.objects.get(username=username)
            messages.warning(request, 'Username is taken')
            return redirect('/auth/signup')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, 'User registered, log you in')
        return redirect('/auth/login')
        
        # You should log the user in after registration
        # user = authenticate(username=username, password=pass1)
        # if user:
        #     login(request, user)

    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)  # Use auth_login instead of login
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')

def logout1(request):
    logout(request)
    messages.success(request,"Logged Out")
    return render(request,'home.html')
