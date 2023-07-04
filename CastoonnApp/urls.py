from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),

    ################################ register
    path('register/',views.register,name='register'),
    
    ]