from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from home.models import Task
from django.db.models import Q

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

from django.db.models import Q

def tasks(request):
    warning=False
    search = request.GET.get('search', '').strip()
    alltask = Task.objects.all()
    if search:
        words = search.split()
        query = Q()
        for word in words:
            query |= Q(tasktitle__icontains=word) | Q(taskdesc__icontains=word)
        alltask = Task.objects.filter(query).distinct()
        if not alltask.exists():
            warning=True
    return render(request, 'tasks.html', {'tasks': alltask,'warning':warning})

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

