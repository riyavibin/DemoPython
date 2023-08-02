from django.contrib import admin
from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('admin/', admin.site.urls),
   #path('homepage/', views.homepage, name='homepage'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('detail/', views.detail, name='detail'),
    #path('thanks/', views.thanks, name='thanks'),
   # path('add/', views.add, name='add'),
]