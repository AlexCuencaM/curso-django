from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseRedirect)
from .forms import TodoForm
from .models import Todo
# Create your views here.
def index(request):
    mensajes = ["Hola vengo desde views :D", "Hola soy una lista de mensajes"]
    mis_credenciales = {
        # clave-valor
        'username': "Alex123",
        'email': "alex@hotmail.com",
        'password': "mi_Ex_es_toxica :V",
    }
    # SELECT * FROM pruebas_django_todo;
    ################
    # Esto es una lista de todo
    # El metodo all nos devuleve una lista de Todo
    todos = Todo.objects.all()

    caballo = "Homer Simpson"
    request.session['caballo'] = caballo
    context = {
        'todos': todos,
        'mensajes': mensajes,
        'caballo': caballo,
        'mis_credenciales': mis_credenciales
    }
    return render(request,'pruebas_django/index.html',context)

    # return HttpResponse("Hola mundo")
def form(request):
    if(request.method == "POST"):
        form = TodoForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data 
            todo = Todo(descripcion= data['descripcion'], done=data['done'])
            todo.save()
            return HttpResponseRedirect('/test/')
    
    if(request.method == "GET"):
        if('caballo' in request.session):
            print(request.session['caballo'])
        else:
            print("No está registrado el caballo :c")
        form = TodoForm()

    return render(request,'pruebas_django/form.html',{'form':form})

def contacts(request):

    if('caballo' in request.session):
        print(request.session['caballo'])
    else:
        print("No está registrado el caballo :c")
    return render(request,'pruebas_django/contacts.html')

def prueba_extend(request):

    return render(request,'pruebas_django/extend_hijo.html')

def test(request, id):
    resultado = "Soy un index con el id:" + str(id)
    return HttpResponse(resultado)
