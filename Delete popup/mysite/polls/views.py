from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
#polls models
from .models import Film, Genre
from .forms import Genreform, Filmform
import csv
#others

def index(request):
    return HttpResponse("Hello, world !")


dot = '.'
def run(request):
    with open(dot+'/media/csv/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        #Film.objects.all().delete()
        #Genre.objects.all().delete()

        for row in reader:
            print(row)

            # genre, _ = Genre.objects.get_or_create(name=row[0])

            film, _ = Film.objects.get_or_create(title=row[1],
                        year=row[2],
                        filmurl = row[3],
                        genre=row[0])
            film.save()
    #return render('base.html')
    return HttpResponse("Hello, world !")

def indexhtml(request):
    filmes = Film.objects.all()
    return render(request, 'films.html', { 'filmes': filmes })


def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        phone=request.POST['phone']
        obj=Film.objects.create(name=name,age=age,phone=phone)
        obj.save()
        return redirect('/')


def retrieve(request):
    details=Film.objects.all()
    return render(request,'retrieve.html',{'details':details})



def edit(request,id):
    object=Film.objects.get(id=id)
    return render(request,'edit.html',{'object':object})

def update(request,id):
    object=Film.objects.get(id=id)
    form=Filmform(request.POST,instance=object)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # object=Film.objects.all()
            return redirect('retrieve')
    return redirect('retrieve')

# def delete(request,id):
#     Film.objects.filter(id=id).delete()
#     return redirect('retrieve')

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Film, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('retrieve')
 
    return render(request, "delete_view.html", context)