import alert as alert
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Department,Courses


# Create your views here.
def index(request):
     return render(request,'index.html')

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

def register(request):
    print(request.method)
    if request.method=='POST':
        username=request.POST['username']


        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password==confirmpassword:
           if User.objects.filter(username=username).exists():
                print("username already exists")
                messages.info(request,"USERNAME Already Exists...")
                return redirect('register')

           else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                print("User Created....")
                return render(request,"login.html")

        else:
         messages.info(request, "Password is not Matched")
         return render(request,"register.html")
    else:
        print("enter else case")
        messages.info(request, "Form is not in method POST")
        return render(request,"register.html")

def regform(request):
    return render(request,"regform.html")

def AllDepartment(request):

    departments = Department.objects.all()
    return render(request,'regform.html',{'department':departments})
def myfunctionq(request):


    return render(request,'confirm.html')
def Getcourse(request):
    print("inside...........")

    id=request.GET.get('deptmnt')
    print(id)
    course = Courses.objects.get(name=id)
    print("get cp")
    return render(request, 'regform.html', {'course': course})
