from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import profile
from .forms import  CustomUserCreationForm
from .utils import searchProfiles





def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password'] 

       try:
           user = User.objects.get(username=username)
       except:
           messages.error(request,'username does not exist')

       user=authenticate(request,username=username,password=password)

       if user is not None:
           login(request,user)
           return redirect('profiles')

       else:
           messages.error(request,'Username OR password is incorrect')        
        
    return render(request,'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'user was logged out')
    return redirect('login')


def registerUser(request):
    page='register'
    form= CustomUserCreationForm()

    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User account was created!')
            login(request,user)
            return redirect('profiles')
        else:
            messages.success(request,'An error occured during registration')    

    context={'page':page, 'form':form}
    return render(request,'users/login_register.html',context)




def profiles(request):
    profiles,search_query=searchProfiles(request)
    '''search_query =''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    skills=skill.objects.filter(name__icontains=search_query)

    profiles=profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills)
        )'''
    context={'profiles':profiles,'search_query':search_query}
    return render(request,'users/profiles.html',context)


def userProfile(request,pk):
    profiles=profile.objects.get(id=pk)

    topskills=profiles.skill_set.exclude(description="")
    otherskills=profiles.skill_set.filter(description="")
    context={'profile':profiles,'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/user-profile.html',context)   

@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    skills=profile.skill_set.all()
    #projects=profile.project_set.all()
    context={'profile':profile,'skills':skills}
    return render(request,'users/account.html',context)    