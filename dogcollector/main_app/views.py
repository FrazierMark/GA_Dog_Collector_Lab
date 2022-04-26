from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse
from .models import Dog



class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

def home(request):
    return HttpResponse('<h1>Hello World!</>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id): # (from urls) path('cats/<int:cat_id>/' <-- this is where cat_id comes from
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})
