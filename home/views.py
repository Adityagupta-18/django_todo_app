from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from home.models import Task
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    context={'success':False}
    if request.method=='POST':
        if not request.user.is_authenticated:
            return redirect('/login/')

        title=request.POST['title']
        desc=request.POST['desc']
        
        ins = Task(
            user=request.user,
            tasktitle=title,
            taskdesc=desc
        )
        ins.save()
        context={'success':True}
    return render(request,'home.html',context)

from django.db.models import Q

@login_required(login_url='/login/')
def tasks(request):
    warning=False
    search = request.GET.get('search', '').strip()
    alltask = Task.objects.filter(user=request.user)    
    if search:
        words = search.split()
        query = Q()
        for word in words:
            query |= Q(tasktitle__icontains=word) | Q(taskdesc__icontains=word)
        alltask = Task.objects.filter(query).distinct()
        if not alltask.exists():
            warning=True
    return render(request, 'tasks.html', {'tasks': alltask,'warning':warning})

@login_required(login_url='/login/')
def edittask(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
       task.tasktitle = request.POST.get("tasktitle")
       task.taskdesc = request.POST.get("taskdesc")
       task.save()
       return redirect("tasks")
    return render(request,"edittask.html",{"task":task})

@login_required(login_url='/login/')
def deltask(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("tasks")


def register_page(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, messages.INFO, "USERNAME ALREADY TAKEN .")
            return redirect('/register/')

        user=User(
            first_name=firstname,
            last_name=lastname,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.INFO, "ACCOUNT CREATED SUCCESSFULLY !")
        return redirect('/register/')

    return render(request,'registerpage.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "USERNAME DOESN'T EXISTS .")
            return redirect('/register/')

        user=authenticate(username=username, password=password)
        if user is None:
            messages.add_message(request, messages.INFO, "INVALID CREDENTIALS .")
        else:
            login(request,user)
            return redirect('tasks')
    return render(request,'loginpage.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')