from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
     ################################ register detail
    path('reg_details/', views.reg_details, name='reg_details'),
    

    ################################ register
    path('register/',views.register,name='register'),
   

    ]