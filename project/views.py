from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from users.models import skill
from .models import project,Tag
from .forms import projectForm

'''projectList = [

            {
              'id':'1',
              'title':"ecommerce website",
              'description':'fully functional ecommerce website'

            },
            {
              'id':'2',
              'title':"portfolio website",
              'description':'this was a project built by myself'
            },
     ]'''





def projects(request):
    search_query =''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tag=Tag.objects.filter(name__icontains=search_query)
    projects=project.objects.distinct().filter(
      Q(title__icontains=search_query)|
      Q(description__icontains=search_query)|
      Q(owner__name__icontains=search_query)|
      Q(tag__in=tag)
      )
    content={'projects':projects,'search_query':search_query}
    return render(request,'pro/projects.html',content)

def panda(request,pk):
    projectobj= project.objects.get(id=pk)
    #tags=projectobj.tag.all()
    '''for i in projectList:
      if i['id']==pk:
        projectobj=i'''
    print('projectobj:',projectobj)    
    return  render(request,'pro/single.html',{'panda':projectobj})


@login_required(login_url="login")
def createproject(request):
    form = projectForm()
    if request.method=='POST':
       form=projectForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
          return redirect('projects')
      
    context = {'form':form}
    return render(request,"pro/project_form.html",context)


@login_required(login_url="login")
def updateproject(request,pk):
    projects = project.objects.get(id=pk)
    form = projectForm(instance=projects)
    if request.method=='POST':
       form=projectForm(request.POST,request.FILES,instance=projects)
       if form.is_valid():
          form.save()
          return redirect('projects')
      
    context = {'form':form}
    return render(request,"pro/project_form.html",context)



@login_required(login_url="login")
def deleteproject(request,pk):
    projects=project.objects.get(id=pk)
    if request.method == 'POST':
      projects.delete()
      return redirect('projects')
    context= {'object':projects}
    return render(request,'pro/delete_template.html',context)







