from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index/index.html')


def register(request):

    return render(request,'index/registerrrr.html')