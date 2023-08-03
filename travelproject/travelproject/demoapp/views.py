from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Meet


# Create your views here.
#def demo(request):
   ## return render(request,"addition.html")
#def demo(request):
  #  return render(request,"index.html")
#def homepage(request):

  # return render(request,"homepage.html")
#def about(request):
    #return HttpResponse("About Us.....")
#def contact(request):
   # return render(request,"contact.html")
#def detail(request):
   # return HttpResponse("Go To Details.....")
#def thanks(request):
   # return render(request,"thanks.html")
#def addition(request):
   # number1=int(request.GET['num1'])
   # number2=int(request.GET['num2'])
   # res1=number1+number2
   # res2=number1-number2
  #  res3=number1*number2
  #  res4=number1/number2

  #  return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
def demo(request):
   # obj=Place.objects.all()

   # print("helo")
   # return render(request,"index.html",{'result':obj},{'result1': obj1})
    obj1 = Meet.objects.all()
    print({'result1': obj1})
    return render(request, "index.html",{'result1': obj1})