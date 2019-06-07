from django.test import TestCase
from django.urls import reverse
from .models import DogBreed, Dog, Review
from django.contrib.auth.models import User
import datetime
from .forms import ProductForm

# Create your tests here.clear
#test for models
class DogBreedTest(TestCase):
    def test_string(self):
        type=DogBreed(dogbreedname='Afghan Hounds')
        self.assertEqual(str(type),type.dogbreedname)
    
    def test_table(self):
        self.assertEqual(str(DogBreed._meta.db_table),'dogbreed')

class DogTest(TestCase):
    def setUp(self):
        self.type=DogBreed(dogbreedname='Alaskan Malammute')
        self.dogbre=Dog(dogname='George',dogbreed=self.type, dogbreedprice=1000.00)
    
    def test_string(self):
        self.assertEqual(str(self.dogbre),self.dogbre.dogname)
    
    def test_type(self):
        self.assertEqual(str(self.dogbre.dogbreed),'Alaskan Malammute')

    def test_discount(self):
        self.assertEqual(self.prod.dogbreedrDiscount()100.00)
        
#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetDogsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=DogBreed.objects.create(dogbreedname='Airedale Terrier')
        self.dogbre=Dog.objects.create(dogname='dog1', dogbreed=self.type, user=self.u, 
        dogbreedprice=500.00,dogbreedentrydate='2019-04-02', dogbreeddescription="some kind of dog")
    
    def test_product_detail_success(self):
        response=self.client.get(reverse('dogbreeddetails', args=(self.dogbre.id,)))
        self.assertEqual(response.status_code, 200)

class ProductFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        self.dog2=DogBreed.objects.create(dogbreedname='dog1')
    
    def test_productForm(self):
        data={
            'dogname' : 'dog1',
            'dogbreed' : self.dog2,
            'user' : self.user2,
            'dogbreedprice' : 1700.00,
            'productentrydate' : datetime.date(2019,6,5),
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_productFormInvalid(self):
        data={
            'dogbreedname' : 'dog1',
            'dogbreed' : 'dog1',
            'user' : self.user2,
            'dogbreedentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())
