from django.shortcuts import render, redirect
from .models import todo
from .forms import todoModelForm

# Create your views here.
def index_todo(request):
    favoritos_lista = todo.objects.all()
    
    contex = {
        'favoritos_lista': favoritos_lista
    }

    return render(request, 'todo/lista.html', contex)


def crear_todo(request):

    form = todoModelForm()


    if request.method == 'POST':

        form = todoModelForm(request.POST)
        if form.is_valid():
           form.save()
        else:
            print(form.erros)
    
    context = {
        'form' :form,
        'titulo':'Crear Favorito'
    }
    return render(request, 'todo/crear.html', context)


def borrar_todo(request, pk):
    todo.objects.get(pk=pk).delete()
    return index_todo(request)


def detalle_todo(request, pk):
    favorito = todo.objects.get(pk=pk)
    return render(request, 'todo/detalle.html', context={'object':favorito})


def actualizar_todo(request, pk):
    favorito = todo.objects.get(pk=pk)

    form = todoModelForm(instance=favorito)


    if request.method == 'POST':

        form = todoModelForm(request.POST, instance=favorito)
        if form.is_valid():
           form.save()
        else:
            print(form.erros)
    
    context = {
        'form' :form,
        'titulo':'Actualizar Favorito'
    }
    return render(request, 'todo/crear.html', context)
