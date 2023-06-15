from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import movie_form
from . models import Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'det':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dis=request.POST.get('dis')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,dis=dis,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def edit_movie(request, id):
    movie=Movie.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
