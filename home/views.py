from django.shortcuts import render , HttpResponse
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