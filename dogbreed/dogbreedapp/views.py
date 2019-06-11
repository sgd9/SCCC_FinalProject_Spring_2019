from django.shortcuts import render, get_object_or_404
from .models import DogBreed, Dog, Review
from .forms import DogbreedForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'dogbreedapp/index.html')

def gettypes(request):
    dogbreed_list=DogBreed.objects.all()
    return render(request, 'dogbreedapp/types.html' ,{'dogbreed_list' : dogbreed_list})

def getdogs(request):
    dogs_list=Dog.objects.all()
    return render(request, 'dogbreedapp/dogs.html', {'dogs_list': dogs_list})

def dogbreeddetails(request, id):
    dogbre=get_object_or_404(Dog, pk=id)
    reviewcount=Review.objects.filter(dog=id).count()
    reviews=Review.objects.filter(dog=id)
    context={
        'dogbre' : dogbre,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'dogbreedapp/dogbreeddetails.html', context=context)

# form view

@login_required
def newdog(request):
     form=DogbreedForm
     if request.method=='POST':
          form=DogbreedForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=DogbreedForm()
     else:
          form=DogbreedForm()
     return render(request, 'dogbreedapp/newdog.html', {'form': form})

def loginmessage(request):
    return render(request, 'dogbreedapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'dogbreedapp/logoutmessage.html')

@login_required
def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm
     return render(request, 'dogbreedapp/newreview.html', {'form' : form})

 