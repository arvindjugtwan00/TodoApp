from django.shortcuts import render,HttpResponseRedirect
from .models import Task
 

# Create your views here.
def home(request):
    context = {'success':False,'name':'Arv'}
    if request.method == "POST":
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        #print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request,'index.html',context)
def tasks(request):
    allTasks = Task.objects.all()
    context= {'tasks':allTasks}
    return render(request,'tasks.html', context)

def search(request):
    #allsearch= Task.object.all()
    query = request.GET['query'] #query is given to form name and id in tasks.html
    allsearch= Task.objects.filter(taskTitle__contains=query)
    context={'searchs' : allsearch}   #instead of context we can use another name also
    return render(request,'search.html',context)
    #return HttpResponse("this is earch")

def delete(request,id):
    
    if(request.method=='POST'):
            gm=Task.objects.get(id=id)
            gm.delete()
            return HttpResponseRedirect('/tasks')

def update(request, id):
    if(request.method=="POST"):
        task=Task.objects.get(id=id)
        task.taskTitle=request.POST['title']
        task.taskDesc=request.POST['desc']
        task.save()
        return HttpResponseRedirect('/tasks')
    else:
     task=Task.objects.get(id=id)
     return render(request,'update.html',{'tasks':task})


 

