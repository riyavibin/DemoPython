import movies as movies
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import forms
from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
            }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})
def addmovie(request):
     print(request.method)
     if request.method=="POST":
         name=request.POST.get('name')
         desc=request.POST.get('desc')
         year=request.POST.get('year')
         img=request.FILES['img']
         print(name,desc,year,img)
         movie=Movie(name=name,desc=desc,year=year,img=img)
         print("saved")
         movie.save()
     # movie1 = Movie.objects.all()
     # context = {
     #     'movie_list': movie1
     # }
     return render(request, 'addmovie.html')




def update(request,id):
    movie=Movie.objects.get(id=id)
    form=forms.MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
         form.save()
         return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')