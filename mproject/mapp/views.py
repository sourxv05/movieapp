from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from .forms import movieform
from .models import movie




def index(request):
    mov=movie.objects.all()
    context={
        'movie_list':mov
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    mov1=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'mov1':mov1})
def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        des=request.POST.get('des',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        mov1=movie(name=name,des=des,year=year,img=img)
        mov1.save()

    return render(request,'add.html')

def edit(request,id):
    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mov':mov})
def delete(request,id):
    if request.method=='POST':
        mov2=movie.objects.get(id=id)
        mov2.delete()
        return redirect('/')
    return render(request,'delete.html')
