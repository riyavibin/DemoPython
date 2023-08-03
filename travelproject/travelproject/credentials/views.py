

from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect




# Create your views here.
def register(request):
    print(request.method)
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password==confirmpassword:
           if User.objects.filter(username=username).exists():
                print("username already exists")
                messages.info(request,"USERNAME Already Exists...")
                return redirect('register')
           elif User.objects.filter(email=email).exists():
                print("email already exists")
                messages.info(request,"Email Already Exist...")
                return redirect('register')
           else:
                user = User.objects.create_user(username=username,password=password, first_name=first_name, last_name=last_name, email=email)
                user.save();
                print("User Created....")
                return redirect('login')

        else:
         messages.info(request, "Password is not Matched")
         return render(request,"register.html")
    else:
        print("enter else case")
        messages.info(request, "Form is not in method POST")
        return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
