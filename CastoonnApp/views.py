from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index/index.html')

def reg_details(request):

    return render(request,'index/reg_details.html')


def register(request):

    return render(request,'index/registerrrr.html')