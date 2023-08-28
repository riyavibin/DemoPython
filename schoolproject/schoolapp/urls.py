from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from schoolapp import views
app_name='schoolapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('myfunctionq', views.myfunctionq, name='myfunctionq'),
    path('AllDepartment', views.AllDepartment, name='AllDepartment'),
    path('Getcourse', views.Getcourse, name='Getcourse'),
    path('register', views.register, name='register'),
    path('regform', views.regform, name='regform'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)