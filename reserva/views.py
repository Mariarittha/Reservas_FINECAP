from django.shortcuts import render, get_object_or_404,redirect
from .models import Reserva,Stand
from .forms import ReservaForm,StandForm
# from  django.contrib.auth import authenticate
# from  django.contrib.auth import login as loginho
# from django.contrib.auth.models import User
# from django.contrib import messages

def index(request):
   
    return render(request,"reserva/index.html")

def mais(request):
   
    return render(request,"reserva/mais.html")

def nos(request):
   
    return render(request,"reserva/nos.html")

def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            
    else:
        form = ReservaForm()
    
    return render(request, "reserva/form.html", {'form':form})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas':reservas
    }
    return render (request, 'reserva/listar.html', context)


def detalhar(request, id):
    reservas = get_object_or_404(Reserva,id=id)
    context = {'reservas': reservas}
    return render(request,'reserva/detalhar.html', context)



def editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    
    if request.method =='POST':
        form = ReservaForm(request.POST,request.FILES,instance=reserva)
        
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reserva/form.html',{'form':form})
        

#apagar

def apagar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar')
    

