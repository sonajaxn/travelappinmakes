
from . import views
from django.urls import path

urlpatterns = [
     path('',views.demo,name='demo'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact.html'),
#     path('add/',views.addition,name='addition'),
#     path('work/',views.work,name='work'),

       path('login/',views.login,name='login'),
]
