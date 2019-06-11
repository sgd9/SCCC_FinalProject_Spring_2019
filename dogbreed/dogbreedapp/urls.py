from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getdogs/', views.getdogs, name='dogs'),
    path('dogbreeddetails/<int:id>', views.dogbreeddetails, name='dogbreeddetails'),
    path('newdog/', views.newdog, name='newdog'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]