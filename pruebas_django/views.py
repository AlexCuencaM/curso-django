from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pruebas_django/index.html')
    # return HttpResponse("Hola mundo")

def contacts(request):
    return render(request,'pruebas_django/contacts.html')

def prueba_extend(request):
    return render(request,'pruebas_django/extend_hijo.html')

def test(request, id):
    resultado = "Soy un index con el id:" + str(id)
    return HttpResponse(resultado)
