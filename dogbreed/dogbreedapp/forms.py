from django import forms
from .models import Dog, DogBreed, Review

class DogbreedForm(forms.ModelForm):
    class Meta:
        model=Dog
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
