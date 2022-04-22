from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Add the Dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age


dogs = [
    Dog('Lolo', 'beagle', 'foul little demon', 3),
    Dog('Sachi', 'boxer', 'diluted tortoise shell', 0),
    Dog('Raven', 'gloden doodle', '3 legged dog', 4)
]


def home(request):
    return HttpResponse('<h1>Hello World!</>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
