from django.shortcuts import render
from .models import DogBreed, Dog, Review

# Create your views here.
def index (request):
    return render(request, 'dogbreedapp/index.html')

def gettypes(request):
    dogbreed_list=DogBreed.objects.all()
    return render(request, 'dogbreedapp/types.html' ,{'dogbreed_list' : dogbreed_list})

def getdogs(request):
    dogs_list=Dog.objects.all()
    return render(request, 'dogbreedapp/dogs.html', {'dogs_list': dogs_list})

 