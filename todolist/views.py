from ast import Delete
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import ToDoList
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/todolist/login/')
def show(request):
    data_todolist = ToDoList.objects.filter(user=request.user)
    jumlahToDo = 0
    for i in data_todolist:
        jumlahToDo+=1

    if request.method == 'POST':
        temp = ToDoList(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        temp.save()
        return JsonResponse({'message': 'success'})


    context = {
        'list_todo': data_todolist,
        'nama': request.user.username,
        'jumlah': jumlahToDo,
        }
    return render(request, "todolist.html", context)


@login_required(login_url='/todolist/login/')
def checklist(request, pk):

    temp = ToDoList.objects.get(id=pk)
    if (temp.is_finished == False):
        temp.is_finished = True
    else :
        temp.is_finished = False
    temp.save()

    return redirect('todolist:show')


@login_required(login_url='/todolist/login/')
def hapus(request, pk):
    item = ToDoList.objects.filter(pk=pk)
    item.delete()
    return redirect('todolist:show')


@login_required(login_url='/todolist/login/')
def tambahin(request):
    context = {}
    if request.method == "POST":
        temp = ToDoList(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show')
    return render(request, "create-task.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
