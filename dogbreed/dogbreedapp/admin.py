from django.contrib import admin
from .models import DogBreed, Dog, Review

# Register your models here.
admin.site.register(DogBreed)
admin.site.register(Dog)
admin.site.register(Review)
