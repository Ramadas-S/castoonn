from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
     # Creator register details
    path('reg_details/', views.creator_reg_details, name='reg_details'),
    #  Artist register detail
    path('artist_reg_details/', views.artist_reg_details, name='artist_reg_details'),
    # register
    path('register/',views.register,name='register'),
    # Creating Creator userprofile
    
    # path('creator_user_profile/',views.creator_user_profile,name='creator_user_profile'),
    

    ]