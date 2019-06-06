from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DogBreed(models.Model):
    dogbreedname=models.CharField(max_length=255)
    dogbreeddescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.dogbreedname
    
    class Meta:
        db_table='dogbreed'
        verbose_name_plural='dogbreeds'

class Dog(models.Model):
    dogname=models.CharField(max_length=255)
    dogbreed =models.ForeignKey(DogBreed, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    dogbreedprice=models.DecimalField(max_digits=10, decimal_places=2)
    dogbreedentrydate=models.DateField()
    dogbreedURL=models.URLField(null=True, blank=True)
    dogbreeddescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.dogname

    def dogbreedDiscount(self):
        discount=.05
        return float(self.dogbreedprice) * discount
    
    def discountedPrice(self):
        discount=self.dogbreedDiscount()
        return float(self.dogbreedprice)-discount

    class Meta:
        db_table='dog'
        verbose_name_plural='dogs'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    dog=models.ForeignKey(Dog,on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    dogbreedrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

