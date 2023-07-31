from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    #path('details/',views.details,name='details')
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdelete')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)