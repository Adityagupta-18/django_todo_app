from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from home.models import Task

# Create your views here.
def home(request):
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        # for model connection
        print(title,desc)
        ins=Task(tasktitle=title,taskdesc=desc)
        ins.save()
        context={'success':True}
    return render(request,'home.html',context)

def tasks(request):
    alltask=Task.objects.all()
    context={'tasks':alltask}
    return render(request,'tasks.html',context)

def edittask(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
       task.tasktitle = request.POST.get("tasktitle")
       task.taskdesc = request.POST.get("taskdesc")
       task.save()
       return redirect("tasks")
    return render(request,"edittask.html",{"task":task})

def deltask(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("tasks")