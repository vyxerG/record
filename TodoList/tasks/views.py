from django.shortcuts import render, redirect
import random
from . models import ToDoApp,Task
from . forms import *

# # It stays above any view we want to block and basically require authentication for.
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages

def homePage(request):
    return render(request, 'home.html')



def index(request):
    try:
        # lst = ['A','B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        # random.shuffle(lst)
        profile = request.user.profile
        tasks = ToDoApp.objects.filter(owner=profile)

        # form = ToDoAppForm()
        form = ToDoAppForm(instance=profile)
        if not request.user.is_authenticated:
            return redirect('account:login')
        if request.method == 'POST':
            form = ToDoAppForm(request.POST)
            profile = request.user.profile
            # profile = Profile.objects.get(id=request.POST.get(id=task.id))

            if form.is_valid():
                # Getting out the user instance so as to set the user to the user field
                user = form.save(commit=False)
                user.owner = profile  # Setting up the user by getting it directly
                form.save()
            return redirect('list')
    except Exception as e:
        messages.error(request, "An Error Occurred!")
        return redirect("list")
        # messages.error(request, e)
    context = {
        # 'ran':lst,
        'tasks':tasks,
        'form':form,
        }
    return render(request, 'tasks/index.html', context)




@login_required(login_url='account:login')
def createTask(request):
    try:
        # projectOBJ = get_object_or_404(ToDoApp, id=pk)
        tasks = ToDoApp.objects.all()
        # task = Task.objects.get(id=tasks.id)
        # form = ToDoAppForm()
        # Getts the current users profile inother to get the project of that user
        profile = request.user.profile
        form = ToDoAppForm(instance=profile)
        if request.method == 'POST':
            form = ToDoAppForm(request.POST)
            # profile = Profile.objects.get(id=request.POST.get(id=task))
            if form.is_valid():
                user = form.save(commit=False)
                user.owner = profile  # Setting up the user by getting it directly
                form.save()
                return redirect('list')
    except Exception as e:
        messages.error(request, "An Error Occurred!")
        return redirect("create-task")
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/createtask.html', context)


@login_required(login_url='account:login')
def updateToDoApp(request, pk):
    # ToDoApp.objects.get(id=90) for checking server error
    try:
        task = ToDoApp.objects.get(id=pk)
        form = ToDoAppForm(instance=task)
        if request.method == 'POST':
            # NOTE: That if you don't pass in the instance=id it will create a new item so for update you would have to use the instance=id
            form = ToDoAppForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('list')
    except Exception as e:
        messages.error(request, "An Error Occurred!")
        return redirect('list')
    context = {
        "form": form,
    }
    return render(request, 'tasks/update.html', context)


@login_required(login_url='account:login')
def deleteTodo(request, pk):
    item = ToDoApp.objects.get(id=pk)
    # profile = request.user.profile  # Gets the present logged in user
    # This allows only the present(loggedin) user/ and the owner of a particular project would be able to delete a particular project.
    # project = profile.todoapp_set.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list')
    context = {
        "item": item,
    }

    return render(request, 'tasks/delete.html', context)


@login_required(login_url='account:login')
def viewToDoList(request, pk):
    viewItem = ToDoApp.objects.get(id=pk)
    context = {
        "viewItem": viewItem,
    }
    return render(request, 'tasks/view_item.html', context)
