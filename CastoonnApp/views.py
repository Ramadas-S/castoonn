from django.shortcuts import render, redirect
from .forms import CreatorUserProfileForm



def index(request):

    return render(request, 'index/index.html')


#creator_reg_details

def creator_reg_details(request):
    if request.method =='POST':
        form = CreatorUserProfileForm(request.POST)
        print(form.name)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = CreatorUserProfileForm()

    return render(request,'index/creator_reg_details.html',{'form':form})


def artist_reg_details(request):

    return render(request,'index/artist_reg_details.html')


def register(request):

    return render(request,'index/registerrrr.html')



# def creator_user_profile(request):
#     if request.mehtod =='POST':
#         form = CreatorUserProfileForm(request.POST)
#         print(form.name)
#         if form.is_valid():
#             form.save()
#             return redirect('register')
#     else:
#         form = CreatorUserProfileForm()
    
#     return render(request,'index/creator_reg_details.html',{'form': form})

